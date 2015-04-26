//
//  ViewController.swift
//  UrbanApp
//
//  Created by Daniil Sargin on 25/04/15.
//  Copyright (c) 2015 Даниил Саргин. All rights reserved.
//

import UIKit
import MapKit
let UAMetersPerLine: Double = 100000


class ViewController: UIViewController, CLLocationManagerDelegate {
    var chosenAnnotation: Pin!

    @IBAction func unwindToMainMapVC(sender: UIStoryboardSegue) {
    }
    @IBOutlet weak var mapView: MKMapView!
    var locationManager = CLLocationManager()
    var areas = [Area]()
    var tapRecognizer: UITapGestureRecognizer?
    
    func parseJSON(data: NSData){
        var error: NSError?
        
    
        let jsonObject: AnyObject! = NSJSONSerialization.JSONObjectWithData(data,
            options: NSJSONReadingOptions.MutableLeaves, error: &error)
        if let err = error {
            print("ERROR: \(error?.description)\n")
        }
        
        if let jsonObject = jsonObject as? [String: AnyObject] where error == nil,
            let jsonData = JSONValue.fromObject(jsonObject)?["data"]?.array {
                print("JSON: OK\n")
                for pinJSON in jsonData {
                    var area = Area(json: pinJSON)
                    print("\(self.areas.count): \(area.circle.subtitle)\n")
                    self.areas.append(area)
                }
            }
    
    }

    func updateMap() {
        dispatch_async(dispatch_get_main_queue(), { [weak self] Void -> Void in
            if let strongSelf = self {
                for area in strongSelf.areas{
                    strongSelf.mapView.removeAnnotation(area.circle)
                    strongSelf.mapView.addAnnotation(area.circle)
                    strongSelf.mapView.removeOverlay(area.circle)
                    strongSelf.mapView.addOverlay(area.circle)
                }
            }
            })
    }
    
    func loadInitialData() {
        var URL = NSURL(string: "http://10.80.7.23:80/")
//        var URL = NSURL(string: "https://data.honolulu.gov/api/views/yef5-h88r/rows.json?accessType=DOWNLOAD");
        let sessionConfig = NSURLSessionConfiguration.defaultSessionConfiguration()
        let session = NSURLSession(configuration: sessionConfig, delegate: nil, delegateQueue: nil)
        let task = session.dataTaskWithURL(URL!, completionHandler:{ [weak self] (data, response, error) -> Void in
            if (error == nil) {
                let statusCode = (response as! NSHTTPURLResponse).statusCode
                println("Success: \(statusCode)")
                
                if let strongSelf = self {
                    strongSelf.parseJSON(data)
                    strongSelf.updateMap()
                }
            } else {
                println("Failure: \(error!.localizedDescription)")
            }
            })
        task.resume()
    }
    
    func handleGesture(){
        var tapPoint = tapRecognizer!.locationInView(mapView)
        var tapCoord = mapView.convertPoint(tapPoint, toCoordinateFromView: mapView)
        var tapLocation = CLLocation(latitude: tapCoord.latitude, longitude: tapCoord.longitude)
        print("tap:\t\(tapCoord.latitude)\t\(tapCoord.longitude)\n")
        if areas.count > 0 {
            mapView.selectAnnotation(areas[0].circle, animated: true)
            print("success\n")
        }
        var rect = mapView.visibleMapRect
        var points = mapView.annotationsInMapRect(rect)
        for point in points {
            if let point = point as? MKAnnotation{
                print("point: \(point.title!)\n")
                var location = CLLocation(latitude: point.coordinate.latitude, longitude: point.coordinate.longitude)
                if location.distanceFromLocation(tapLocation) < 500 {
                    print("Bingo!\n")
                }
            }
        }
        
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        mapView.delegate = self
        tapRecognizer = UITapGestureRecognizer(target: self, action: Selector("handleGesture"))
        mapView!.addGestureRecognizer(tapRecognizer!)
        tapRecognizer?.delaysTouchesBegan = false
        tapRecognizer?.delaysTouchesEnded = false
        tapRecognizer?.cancelsTouchesInView = false
        loadInitialData()
    }
    
    override func viewWillAppear(animated: Bool) {
        super.viewWillAppear(animated)
        //Moscow
        var zoomLocation = CLLocationCoordinate2D(latitude: 55.75, longitude: 37.6)
        //example city Honolulu with red points
//        let zoomLocation = CLLocationCoordinate2D(latitude: 21.282778, longitude: -157.829444)
        
        let viewRegion = MKCoordinateRegionMakeWithDistance(zoomLocation, 0.5 * UAMetersPerLine, 0.5 * UAMetersPerLine);
        mapView.setRegion(viewRegion, animated: true)
    }

    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        if segue.identifier == "showPinInformation" {
            var DestVC = segue.destinationViewController as! UAPinInfoVC
            DestVC.annotation = chosenAnnotation
        }
    }
}


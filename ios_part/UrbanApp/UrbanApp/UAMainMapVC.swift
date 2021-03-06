//
//  ViewController.swift
//  UrbanApp
//
//  Created by Daniil Sargin on 25/04/15.
//  Copyright (c) 2015 Даниил Саргин. All rights reserved.
//

import UIKit
import MapKit
let UAMetersPerLine: Double = 50000


class ViewController: UIViewController, CLLocationManagerDelegate {
    var chosenAnnotation: Pin!

    @IBOutlet weak var refreshButton: UIButton!
    @IBAction func unwindToMainMapVC(sender: UIStoryboardSegue) {
    }
    @IBOutlet weak var mapView: MKMapView!
    var locationManager = CLLocationManager()
    var pins = [Pin]()
    
    func parseJSON(data: NSData) {
        var error: NSError?
        let jsonObject: AnyObject! = NSJSONSerialization.JSONObjectWithData(data,
            options: NSJSONReadingOptions(0), error: &error)
        
        if let jsonObject = jsonObject as? [String: AnyObject] where error == nil,
            let jsonData = JSONValue.fromObject(jsonObject)?["data"]?.array {
                for pinJSON in jsonData {
                    var pin = Pin(json: pinJSON)
                    print("\(self.pins.count): \(pin.subtitle)\n")
                    self.pins.append(pin)
                }
        }
    }

    func updateMap() {
        dispatch_async(dispatch_get_main_queue(), { [weak self] Void -> Void in
            if let strongSelf = self {
                strongSelf.mapView.removeAnnotations(strongSelf.pins)
                strongSelf.mapView.addAnnotations(strongSelf.pins)
                strongSelf.refreshButton.hidden = false
            }
            })
    }
    
    func loadInitialData() {
        var URL = NSURL(string: "http://10.80.7.23:80/")
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
    
    
    @IBAction func refreshButtonPressed(sender: AnyObject) {
        refreshButton.hidden = true
        loadInitialData()
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        self.refreshButton.hidden = true
        mapView.delegate = self
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


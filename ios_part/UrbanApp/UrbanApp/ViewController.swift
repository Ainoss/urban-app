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
    @IBOutlet weak var mapView: MKMapView!
    var locationManager = CLLocationManager()
    var pins = [Pin]()
    
    func loadInitialData() {
        let fileName = NSBundle.mainBundle().pathForResource("PublicArt", ofType: "json");
        var readError : NSError?
        var data: NSData = NSData(contentsOfFile: fileName!, options: NSDataReadingOptions(0),
            error: &readError)!
        
        var error: NSError?
        let jsonObject: AnyObject! = NSJSONSerialization.JSONObjectWithData(data,
            options: NSJSONReadingOptions(0), error: &error)
        
        if let jsonObject = jsonObject as? [String: AnyObject] where error == nil,
            let jsonData = JSONValue.fromObject(jsonObject)?["data"]?.array {
                for pinJSON in jsonData {
                    if let pinJSON = pinJSON.array,
                        pin = Pin.fromJSON(pinJSON) {
                            pins.append(pin)
                    }
                }
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        mapView.delegate = self
        loadInitialData()
        mapView.addAnnotations(pins)
        // Do any additional setup after loading the view, typically from a nib.
    }

    
    override func viewWillAppear(animated: Bool) {
        super.viewWillAppear(animated)
        //example city with red points
//        var zoomLocation = CLLocationCoordinate2D(latitude: 55.75, longitude: 37.616667) 
        //Moscow
        let zoomLocation = CLLocationCoordinate2D(latitude: 21.282778, longitude: -157.829444)
        
        let viewRegion = MKCoordinateRegionMakeWithDistance(zoomLocation, 0.5 * UAMetersPerLine, 0.5 * UAMetersPerLine);
        mapView.setRegion(viewRegion, animated: true)
    }

}


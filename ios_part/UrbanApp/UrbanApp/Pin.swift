//
//  Pin.swift
//  UrbanApp
//
//  Created by Daniil Sargin on 25/04/15.
//  Copyright (c) 2015 Даниил Саргин. All rights reserved.
//

import Foundation
import MapKit

class Pin: NSObject, MKAnnotation {
    let coordinate: CLLocationCoordinate2D
    let title: String
    var subtitle: String
    let locationName: String
    let locationSize: Int
    let pinColor: MKPinAnnotationColor = .Red
    var paths = [String]()
    
    var messages = [String]()
    
    init(title: String, subtitle: String, locationName: String, locationSize: Int, coordinate: CLLocationCoordinate2D) {
        self.title = title
        self.subtitle = "subtitle"
        self.locationName = locationName
        self.coordinate = coordinate
        self.locationSize = locationSize
        
        super.init()
    }
    
    init(json: JSONValue) {
        title = "Tweets"
        locationName = title
        locationSize = json["size"]!.integer!
        let longitude = (json["longitude"]!.string! as NSString).doubleValue
        let latitude = (json["latitude"]!.string! as NSString).doubleValue
        coordinate = CLLocationCoordinate2D(latitude: latitude, longitude: longitude)
        var messagesData = json["messages"]!.array!
        var cnt: Int = 0
        for msg in messagesData {
            if (cnt % 2) == 0 {
                messages.append(msg.string!)
            }
            else {
                paths.append(msg.string!)
            }
            cnt++
        }
        if messages.count > 0{
            subtitle = json["messages"]!.array![0].string!
            
        }
        else {
            subtitle = ""
            
        }
    }
    
}

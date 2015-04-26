//
//  Pin.swift
//  UrbanApp
//
//  Created by Daniil Sargin on 25/04/15.
//  Copyright (c) 2015 Даниил Саргин. All rights reserved.
//

import Foundation
import MapKit

class Area: NSObject {
    let circle: MKCircle
    let locationName: String
    let locationSize: Int    
    var messages = [String]()
    

    init(json: JSONValue) {
        var messagesData = json["messages"]!.array!
        for msg in messagesData {
            messages.append(msg.string!)
        }
        locationName = "Title"
        locationSize = json["size"]!.integer!
        
        let longitude = (json["longitude"]!.string! as NSString).doubleValue
        let latitude = (json["latitude"]!.string! as NSString).doubleValue
        var coordinate = CLLocationCoordinate2D(latitude: latitude, longitude: longitude)
        var radius = Double(500.0)
        circle = MKCircle(centerCoordinate: coordinate, radius: radius)
        
        circle.title = locationName
        if messages.count > 0{
            circle.subtitle = messages[0]
        }
        else{
            print("No message\n")
        }
        
    }
    
}

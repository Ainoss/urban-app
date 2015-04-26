//
//  VCMapView.swift
//  UrbanApp
//
//  Created by Daniil Sargin on 25/04/15.
//  Copyright (c) 2015 Даниил Саргин. All rights reserved.
//

import Foundation

import MapKit

extension ViewController: MKMapViewDelegate {
    func mapView(mapView: MKMapView!, viewForAnnotation annotation: MKAnnotation!) -> MKAnnotationView! {
        if let annotation = annotation {
            let identifier = "area"
            var view: MKAnnotationView
            if let dequeuedView = mapView.dequeueReusableAnnotationViewWithIdentifier(identifier) { 		
                    dequeuedView.annotation = annotation
                    view = dequeuedView
            } else {
                view = MKAnnotationView(annotation: annotation, reuseIdentifier: identifier)
                view.canShowCallout = true
                view.calloutOffset = CGPoint(x: -5, y: 5)
                view.rightCalloutAccessoryView = UIButton.buttonWithType(.DetailDisclosure) as! UIView
                view.enabled = false
            }
            //view.image = UIImage(named: "Area_mid")
            //var frame = CGRect(origin: view.frame.origin, size: view.frame.size)
            //frame.size.width = CGFloat(Float(mapView.bounds.width) * Float(mapView.visibleMapRect.size.width) / 10.0 / 1000.0)
            //frame.size.height = frame.size.width
            //print("\(mapView.visibleMapRect.size.height)\n")
            //view.frame = frame

            return view
        }
        return nil
    }
    
    func mapView(mapView: MKMapView!, annotationView view: MKAnnotationView!,
        calloutAccessoryControlTapped control: UIControl!) {
            let location = view.annotation as! Pin
            chosenAnnotation = location
            let launchOptions = [MKLaunchOptionsDirectionsModeKey: MKLaunchOptionsDirectionsModeDriving]
            performSegueWithIdentifier("showPinInformation", sender: nil)
//            showPinInformation
//            location.mapItem().openInMapsWithLaunchOptions(launchOptions)
            
            
    }
    
    func mapView(mapView: MKMapView!, rendererForOverlay overlay: MKOverlay!) -> MKOverlayRenderer! {
        if let overlay = overlay as? MKCircle{
            let identifier = "circle"
            var renderer = MKCircleRenderer(circle: overlay)
            renderer.fillColor = UIColor.colorWithAlphaComponent(UIColor.blueColor())(0.5)
            return renderer
        }
        return nil
    }
}
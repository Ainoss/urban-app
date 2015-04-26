//
//  UAPinInfoVC.swift
//  UrbanApp
//
//  Created by Daniil Sargin on 25/04/15.
//  Copyright (c) 2015 Даниил Саргин. All rights reserved.
//

import UIKit

class UAPinInfoVC: UIViewController, UITableViewDataSource, UITableViewDelegate {
    var annotation: Pin!
    var didAppear: Bool = false
    @IBOutlet weak var tableView: UITableView!
//    var imagePath = ""
    var imagePath = "https://d25l0qqym3malo.cloudfront.net/engines/im/images/logo.png"
    
    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.dataSource = self
        tableView.delegate = self
        tableView.rowHeight = UITableViewAutomaticDimension
        tableView.estimatedRowHeight = 160.0
    }
    
    override func viewDidAppear(animated: Bool) {
        super.viewDidAppear(animated)
        didAppear = true
        self.tableView.reloadData()
    }

    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return annotation.messages.count
    }
    
//TODO:
    func hasImageForIndexPath(indexPath: NSIndexPath) -> Bool {
        return (annotation.paths[indexPath.row] == "") ? false : true
    }
    
    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        if hasImageForIndexPath(indexPath) {
            return imageCellAtIndexPath(indexPath)
        } else {
            return textCellAtIndexPath(indexPath)
        }
    }
    
    func imageCellAtIndexPath(indexPath:NSIndexPath) -> UAImageCell {
        let cell = tableView.dequeueReusableCellWithIdentifier("imageCell") as! UAImageCell
        setTimeForCell(cell, indexPath: indexPath)
        setMessageForCell(cell, indexPath: indexPath)
        setImageForCell(cell, indexPath: indexPath)
        return cell
    }
    
//TODO:
    func setImageForCell(cell:UAImageCell, indexPath:NSIndexPath) {
        let item: String = annotation.paths[indexPath.row]
        cell.photoView.image = nil
        if let url = NSURL(string: item) {
            if didAppear {
                cell.photoView.setImageWithURL(url)
            }
        }
    }
    
    func textCellAtIndexPath(indexPath:NSIndexPath) -> UATextCell {
        let cell = tableView.dequeueReusableCellWithIdentifier("textCell") as! UATextCell
        setTimeForCell(cell, indexPath: indexPath)
        setMessageForCell(cell, indexPath: indexPath)
        return cell
    }
    
    func setMessageForCell(cell:UATextCell, indexPath:NSIndexPath) {
        let item = annotation.messages[indexPath.row] as String
        cell.messageText.text = didAppear ? (item ?? "[No Title]") : ""
    }
    
    func setTimeForCell(cell:UATextCell, indexPath:NSIndexPath) {
        let item = annotation.title as String
        cell.timeText.text = didAppear ? (item ?? "[No Title]") : ""
    }

    
}

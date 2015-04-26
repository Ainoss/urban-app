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
    
    @IBOutlet weak var tableView: UITableView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.dataSource = self
        tableView.delegate = self
        tableView.rowHeight = UITableViewAutomaticDimension
        tableView.estimatedRowHeight = 160.0
    }
    
    override func viewDidAppear(animated: Bool) {
        super.viewDidAppear(animated)
        self.tableView.reloadData()
    }
    
    func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        return 1
    }

    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return annotation.messages.count;
    }
    
    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        var cell: UATextCell = self.tableView.dequeueReusableCellWithIdentifier("cell1", forIndexPath: indexPath) as! UATextCell
        cell.timeText.text = annotation.messages[indexPath.indexAtPosition(0)]
        cell.messageText.text = annotation.messages[indexPath.indexAtPosition(1)]
//        println(indexPath.indexAtPosition(1))
//        println(cell.messageText.text)
        return cell
    }
    
}

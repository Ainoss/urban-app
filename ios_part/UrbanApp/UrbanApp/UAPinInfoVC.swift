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
    }
    
    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return 0;
    }
    
    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        return UITableViewCell()
    }
    
}

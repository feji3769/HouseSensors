//
//  House.swift
//  HouseStatus
//
//  Created by Felix Jimenez on 4/20/20.
//  Copyright © 2020 Felix Jimenez. All rights reserved.
//

import SwiftUI

struct House: Hashable, Codable{
    var id: Int
    var name: String
    var imageName: String
    
}


extension House {
    var image: Image {
        ImageStore.shared.image(name: imageName)
    }
}

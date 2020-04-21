//
//  HouseDetail.swift
//  HouseStatus
//
//  Created by Felix Jimenez on 4/20/20.
//  Copyright © 2020 Felix Jimenez. All rights reserved.
//

import SwiftUI

struct HouseDetail: View {
    var house: House
    
    var body: some View {
        VStack{
            Text(house.name)
        }
    }
}

struct HouseDetail_Previews: PreviewProvider {
    static var previews: some View {
        HouseDetail(house: houseData[0])
    }
}

//
//  HouseRow.swift
//  HouseStatus
//
//  Created by Felix Jimenez on 4/20/20.
//  Copyright © 2020 Felix Jimenez. All rights reserved.
//

import SwiftUI

struct HouseRow: View {
    var house: House
    
    var body: some View {
        
        HStack {
            house.image
                .resizable()
                .frame(width: 50, height: 50)
            Text(house.name)
            Spacer()
        }
    }
}

struct HouseRow_Previews: PreviewProvider {
    static var previews: some View {
        HouseRow( house: houseData[0])
    }
}

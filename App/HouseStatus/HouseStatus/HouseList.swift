//
//  HouseList.swift
//  HouseStatus
//
//  Created by Felix Jimenez on 4/20/20.
//  Copyright © 2020 Felix Jimenez. All rights reserved.
//

import SwiftUI

struct HouseList: View {
    var body: some View {
        NavigationView{
            List(houseData, id: \.id) { house in
                NavigationLink(destination: HouseDetail(house: house))
                {HouseRow(house: house)}
                
            }
        }.navigationBarTitle(Text("Houses"))
    }
}

struct HouseList_Previews: PreviewProvider {
    static var previews: some View {
        HouseList()
    }
}


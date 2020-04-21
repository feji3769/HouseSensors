//
//  ContentView.swift
//  HouseStatus
//
//  Created by Felix Jimenez on 4/20/20.
//  Copyright © 2020 Felix Jimenez. All rights reserved.
//

import SwiftUI

struct ContentView: View {
    @State private var selection = 0
 
    var body: some View {
        TabView(selection: $selection){
            VStack{
                HomePage()
            }
                .font(.title)
                .tabItem {
                    VStack {
                        Image("first")
                        Text("Home")
                    }
                }
                .tag(0)
            VStack{HouseList()}
                .font(.title)
                .tabItem {
                    VStack {
                        Image("second")
                        Text("House List").font(.title).foregroundColor(.green)
                    }
                }
                .tag(1)
            VStack{HelpPage()}
                .font(.title)
                .tabItem {
                    VStack {
                        Image("second")
                        Text("Help")
                    }
                }
                .tag(2)
        }
    }
}





struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

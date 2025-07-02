#![allow(dead_code)]
#![allow(unused_imports)]
#![allow(unused_variables)]

// https://blog.dbrgn.ch/2019/12/24/testing-for-no-std-compatibility/
// https://github.com/hobofan/cargo-nono
#![no_std]

// https://github.com/stm32-rs/stm32-eth/blob/master/examples/rtic-echo.rs
// #![no_main]

// flatbuffers, tokio or rtic/smoltcp, rustls

extern crate alloc;
use alloc::boxed::Box;

/*
extern crate flexbuffers;
extern crate serde;
use serde::{Deserialize, Serialize};
 */

use flatbuffers::FlatBufferBuilder;
mod auth_generated;
mod pubsub_generated;
mod roles_generated;
mod rpc_generated;
mod session_generated;
mod types_generated;
mod wamp_generated;
use rpc_generated::wamp::proto::Cancel;
use rpc_generated::wamp::proto::CancelArgs;

/*
#[derive(Debug, PartialEq, Serialize, Deserialize)]
struct Color(u8, u8, u8, u8);

#[derive(Debug, PartialEq, Serialize, Deserialize)]
struct Monster {
    hp: u32,
    mana: i32,
    enraged: bool,
    // weapons: Vec<Weapon>,
    color: Color,
    position: [f64; 3],
    velocity: [f64; 3],
    // coins: Vec<u32>,
}
 */

fn main() {
    let data: Box<[u8]> = Box::new([0; 8192]);
    // println!("{:?}", data.len());

    let mut fbb = flatbuffers::FlatBufferBuilder::new();

    let table = fbb.start_table();
    fbb.push_slot(Cancel::VT_REQUEST, 63u64, 0u64);
    fbb.push_slot(
        Cancel::VT_MODE,
        types_generated::wamp::proto::CancelMode::KILL,
        types_generated::wamp::proto::CancelMode::SKIP,
    );
    let root = fbb.end_table(table);
    fbb.finish(root, None);
    let data1 = fbb.finished_data();
    // println!("{:?}", data1);

    let args1 = rpc_generated::wamp::proto::CancelArgs {
        request: 63,
        mode: types_generated::wamp::proto::CancelMode::SKIP,
        forward_for: None,
    };

    let msg1 = Cancel::create(&mut fbb, &args1);
    // println!("{:?}", msg1);

    /*
    let mut s = flexbuffers::FlexbufferSerializer::new();
    msg1.serialize(&mut s).unwrap();

    let monster = Monster {
           hp: 80,
           mana: 200,
           enraged: true,
           color: Color(255, 255, 255, 255),
           position: [0.0; 3],
           velocity: [1.0, 0.0, 0.0],
           // weapons: vec![
           //     Weapon::Fist,
           //     Weapon::Equipment {
           //         name: "great axe".to_string(),
           //         damage: 15,
           //     },
           //     Weapon::Equipment {
           //         name: "hammer".to_string(),
           //         damage: 5,
           //     },
           // ],
           // coins: vec![5, 10, 25, 25, 25, 100],
       };
       let mut s = flexbuffers::FlexbufferSerializer::new();
       monster.serialize(&mut s).unwrap();

       let r = flexbuffers::Reader::get_root(s.view()).unwrap();

       let monster2 = Monster::deserialize(r).unwrap();

       assert_eq!(monster, monster2);
    */
}

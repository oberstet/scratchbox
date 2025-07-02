#![allow(incomplete_features)]
#![feature(async_fn_in_trait)]

// requires: rustup default nightly && rustup update

// trait Rows {
//     type Row;
//     async fn next(&mut self) -> Option<Self::Row>;
// }
use serde::{Deserialize, Serialize};
use std::error::Error;

//use serde_json;
use serde_cbor;

#[derive(Serialize, Deserialize, Debug)]
struct Mascot {
    name: String,
    species: String,
    year_of_birth: u32,
}

fn main() -> Result<(), Box<dyn Error>> {
    let ferris = Mascot {
        name: "Ferris".to_owned(),
        species: "crab".to_owned(),
        year_of_birth: 2015,
    };

    let serialized = serde_cbor::to_vec(&ferris).unwrap();
    println!("serialized = {:?}", serialized);

    let deserialized: Mascot = serde_cbor::from_slice(&serialized).unwrap();
    println!("deserialized = {:?}", deserialized);

    Ok(())
}
trait Database {
    async fn fetch_data(&self) -> String;
    // fn fetch_rows(&self) -> Rows;
}

struct MyDB {

}

impl Database for MyDB {
    async fn fetch_data(&self) -> String {
        "Hello, world!".to_string()
    }
}

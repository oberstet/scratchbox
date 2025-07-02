// rustup install nightly
// cargo +nightly build
// cargo +nightly build --target x86_64-unknown-linux-gnu

// // #![no_main]
#![no_std]
#![feature(lang_items, libc)]

#![feature(default_alloc_error_handler)]

// #![feature(default_alloc_error_handler)]

// // https://stackoverflow.com/questions/37843379/is-it-possible-to-use-box-with-no-std
// extern crate alloc;
// use alloc::boxed::Box;
// use alloc::alloc::Allocator;

// /// The static global allocator.
// #[global_allocator]
// static GLOBAL_ALLOCATOR: Allocator = Allocator;


//#![cfg_attr(not(feature = "std"), no_std)]

//#[cfg(feature = "std")]
// extern crate core;

//#[cfg(feature = "alloc")]
extern crate alloc;
use alloc::boxed::Box;


// https://doc.rust-lang.org/nomicon/panic-handler.html
use core::panic::PanicInfo;

#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {}
}




extern crate good_memory_allocator;

// https://crates.io/crates/good_memory_allocator
use good_memory_allocator::SpinLockedAllocator;

#[global_allocator]
static ALLOCATOR: SpinLockedAllocator = SpinLockedAllocator::empty();

// pub fn init_heap() {
//     unsafe {
//         ALLOCATOR.init(heap_start, heap_size);
//     }
// }




extern crate libc;

use libc::c_char;
// use std::collections::HashMap;
// use std::ffi::CStr;


pub struct ZipCodeDatabase {
    // population: HashMap<String, u32>,
}

impl ZipCodeDatabase {
    fn new() -> ZipCodeDatabase {
        ZipCodeDatabase {
            // population: HashMap::new(),
        }
    }

    fn populate(&mut self) {
        // for i in 0..100_000 {
        //     let zip = format!("{:05}", i);
        //     self.population.insert(zip, i);
        // }
    }

    fn population_of(&self, zip: &str) -> u32 {
        // self.population.get(zip).cloned().unwrap_or(0)
        0
    }
}

#[no_mangle]
pub extern "C" fn zip_code_database_new() -> *mut ZipCodeDatabase {
    Box::into_raw(Box::new(ZipCodeDatabase::new()))
}

#[no_mangle]
pub extern "C" fn zip_code_database_free(ptr: *mut ZipCodeDatabase) {
    if ptr.is_null() {
        return;
    }
    unsafe {
        Box::from_raw(ptr);
    }
}

#[no_mangle]
pub extern "C" fn zip_code_database_populate(ptr: *mut ZipCodeDatabase) {
    let database = unsafe {
        assert!(!ptr.is_null());
        &mut *ptr
    };
    database.populate();
}

#[no_mangle]
pub extern "C" fn zip_code_database_population_of(
    ptr: *const ZipCodeDatabase,
    zip: *const c_char,
) -> u32 {
    // let database = unsafe {
    //     assert!(!ptr.is_null());
    //     &*ptr
    // };
    // let zip = unsafe {
    //     assert!(!zip.is_null());
    //     CStr::from_ptr(zip)
    // };
    // let zip_str = zip.to_str().unwrap();
    // database.population_of(zip_str)
    0
}

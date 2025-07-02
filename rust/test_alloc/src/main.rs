#![no_std]
#![feature(alloc_error_handler)]
extern crate alloc;

use alloc::alloc::{GlobalAlloc, Layout};
use core::alloc::LayoutErr;
use core::ops::Deref;
use core::ptr::NonNull;
use alloc::string::String;
use alloc::vec::Vec;
use alloc::collections::btree_map::BTreeMap;
use alloc::collections::HashMap;

struct MyAllocator;

unsafe impl GlobalAlloc for MyAllocator {
    unsafe fn alloc(&self, layout: Layout) -> *mut u8 {
        // implementation of the allocator's `alloc` method
    }

    unsafe fn dealloc(&self, ptr: *mut u8, layout: Layout) {
        // implementation of the allocator's `dealloc` method
    }

    fn usable_size(&self, layout: &Layout) -> (usize, usize) {
        // implementation of the allocator's `usable_size` method
    }

    fn allocate(&self, layout: Layout) -> Result<NonNull<[u8]>, LayoutErr> {
        // implementation of the allocator's `allocate` method
    }

    unsafe fn deallocate(&self, ptr: NonNull<u8>, layout: Layout) {
        // implementation of the allocator's `deallocate` method
    }
}

#[global_allocator]
static GLOBAL: MyAllocator = MyAllocator;

#[alloc_error_handler]
fn on_oom(_: Layout) -> ! {
    panic!("Out of memory");
}

fn main() {
    let mut my_vec: Vec<u32> = Vec::new();
    my_vec.push(1);
    my_vec.push(2);
    my_vec.push(3);

    let mut my_map: HashMap<&str, u32> = HashMap::new();
    my_map.insert("one", 1);
    my_map.insert("two", 2);
    my_map.insert("three", 3);

    let my_string = String::from("Hello, world!");

    println!("{:?}", my_vec);
    println!("{:?}", my_map);
    println!("{}", my_string);
}

#![no_std]
#![feature(allocator_api)]
#![feature(alloc_ref)]
#![feature(alloc_error_handler)]

extern crate alloc;
use alloc::alloc::{GlobalAlloc, AllocError, Layout};

//use buddy_alloc::{BuddyAlloc, BuddyBox};
use buddy_alloc::{BuddyAllocParam, FastAllocParam, NonThreadsafeAlloc};

//use core::alloc::{Alloc, Layout};
//use core::panic::PanicInfo;


use serde::{Deserialize, Serialize};
use serde_cbor::{from_slice, to_vec};

const FAST_HEAP_SIZE: usize = 32 * 1024; // 32 KB
const HEAP_SIZE: usize = 1024 * 1024; // 1M
const LEAF_SIZE: usize = 16;

pub static mut FAST_HEAP_1: [u8; FAST_HEAP_SIZE] = [0u8; FAST_HEAP_SIZE];
pub static mut HEAP_1: [u8; HEAP_SIZE] = [0u8; HEAP_SIZE];

pub static mut FAST_HEAP_2: [u8; FAST_HEAP_SIZE] = [0u8; FAST_HEAP_SIZE];
pub static mut HEAP_2: [u8; HEAP_SIZE] = [0u8; HEAP_SIZE];

// extern crate alloc;

// use alloc::alloc::{GlobalAlloc, Layout};
use alloc::vec::Vec;
use alloc::string::String;

// use core::alloc::{Allocator, AllocError, LayoutErr};
// use core::alloc::{Alloc, LayoutErr, AllocErr};

// use core::fmt::Debug;
// use core::marker::PhantomData;

// Custom allocator #1
// struct MyAllocator1;

// unsafe impl GlobalAlloc for MyAllocator1 {
//     unsafe fn alloc(&self, layout: Layout) -> *mut u8 {
//         // Implementation of allocation method for MyAllocator1
//         // ...
//     }

//     unsafe fn dealloc(&self, ptr: *mut u8, layout: Layout) {
//         // Implementation of deallocation method for MyAllocator1
//         // ...
//     }
// }

// // Custom allocator #2
// struct MyAllocator2;

// unsafe impl GlobalAlloc for MyAllocator2 {
//     unsafe fn alloc(&self, layout: Layout) -> *mut u8 {
//         // Implementation of allocation method for MyAllocator2
//         // ...
//     }

//     unsafe fn dealloc(&self, ptr: *mut u8, layout: Layout) {
//         // Implementation of deallocation method for MyAllocator2
//         // ...
//     }
// }

// #![feature(allocator_api)]

// struct Box<T, A: AllocRef = Global>(T, A);

// #[global_allocator]
// static GLOBAL1: MyAllocator1 = MyAllocator1;
// static GLOBAL2: MyAllocator2 = MyAllocator2;

// #[alloc_error_handler]
// fn on_oom(_: Layout) -> ! {
//     panic!("Out of memory");
// }

// https://dev-doc.rust-lang.org/beta/std/alloc/trait.AllocRef.html

// Vec<u8>
// Box<T, A=Global>
// Vec<T, A>

// https://github.com/rust-lang/wg-allocators/issues/7
// https://not-matthias.github.io/posts/rust-kernel-adventures/
// https://doc.rust-lang.org/beta/unstable-book/library-features/allocator-api.html
// https://docs.rs/ciborium/latest/ciborium/
// https://docs.rs/minicbor/latest/minicbor/
// https://crates.io/crates/ciborium-io
// https://crates.io/crates/hashbrown
// https://github.com/enarx/ciborium/blob/main/ciborium-io/src/lib.rs
// https://lib.rs/crates/mimalloc
// https://lib.rs/keywords/allocator
// https://lib.rs/crates/linked_list_allocator


// A helper function that serializes a value to CBOR format using a given allocator
fn serialize_with_allocator<T, A>(value: &T, allocator: A) -> Vec<u8>
where
    T: serde::Serialize,
    A: GlobalAlloc + core::alloc::Allocator,
{
    let mut buffer = Vec::new_in(allocator);
    let mut serializer = serde_cbor::Serializer::new(&mut buffer).with_allocator(allocator);
    value.serialize(&mut serializer).unwrap();
    buffer
}

// A helper function that deserializes a value from CBOR format using a given allocator
fn deserialize_with_allocator<'a, T, A>(data: &'a [u8], allocator: A) -> T
where
    T: serde::Deserialize<'a>,
    A: GlobalAlloc + core::alloc::Allocator,
{
    let mut deserializer =
        serde_cbor::Deserializer::from_slice(data).with_allocator(allocator);
    T::deserialize(&mut deserializer).unwrap()
}

// This allocator can't work in tests since it's non-threadsafe.
// #[cfg_attr(not(test), global_allocator)]
// static ALLOC: NonThreadsafeAlloc = unsafe {
//     let fast_param = FastAllocParam::new(FAST_HEAP.as_ptr(), FAST_HEAP_SIZE);
//     let buddy_param = BuddyAllocParam::new(HEAP.as_ptr(), HEAP_SIZE, LEAF_SIZE);
//     NonThreadsafeAlloc::new(fast_param, buddy_param)
// };


fn main() {
    let fast_param_1 = FastAllocParam::new(FAST_HEAP_1.as_ptr(), FAST_HEAP_SIZE);
    let buddy_param_1 = BuddyAllocParam::new(HEAP_1.as_ptr(), HEAP_SIZE, LEAF_SIZE);
    let alloc_1 = NonThreadsafeAlloc::new(fast_param_1, buddy_param_1);

    // Serialize a value using MyAllocator1
    let value1 = "hello, world";
    let cbor1 = serialize_with_allocator(&value1, alloc_1);

    // Deserialize the value using MyAllocator2
    let value2: String = deserialize_with_allocator(&cbor1, alloc_1);
}

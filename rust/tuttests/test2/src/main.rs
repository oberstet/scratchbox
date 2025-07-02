use libp2p::gossipsub::TopicHash;
use core::fmt;

#[derive(Debug)]
struct Point2D {
    x: f64,
    y: f64,
}

impl Point2D {
    fn move_right(self, distance: f64) -> Point2D {
        Point2D {
            x: self.x + distance,
            y: self.y,
        }
    }
}

impl fmt::Display for Point2D {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{} {}", self.x, self.y)
    }
}

#[derive(Debug)]
struct AppendOnlyVec<T> {
    inner: Vec<T>,
}

impl<T> AppendOnlyVec<T> {
    fn new(v: Vec<T>) -> AppendOnlyVec<T> {
        AppendOnlyVec { inner: v }
    }

    fn push(&mut self, el: T) {
        self.inner.push(el);
    }

    fn into_vec(&self) -> Vec<T> {
        let v: Vec<T> = vec!();
        // v.copy_from_slice(&self.inner);
        v
    }
}

fn main() {
    // let p = Point2D();
    let p = Point2D { x: 23.0, y: 666.0 };
    println!("{:?}", p);
    let p2 = p.move_right(100.0);
    println!("{:?}", p2);

    let mut v = AppendOnlyVec::new(vec![1.0, 2.0, 3.0]);

    println!("{:?}", v);
    // println!("{:?}", v.into_vec());

    v.push(55.8);

    println!("{:?}", v);

    let iv2 = v.into_vec();
    println!("{:?}", iv2);

    v.push(333.333);

    let t1 = TopicHash::from_raw("com.example.myapp.procedure1");
    println!("{:?}", t1);
}

// https://doc.rust-lang.org/stable/std/sync/mpsc/index.html
// https://tokio.rs/tokio/tutorial/channels

// std::sync::mpsc
// crossbeam::channel
// tokio::sync::mpsc
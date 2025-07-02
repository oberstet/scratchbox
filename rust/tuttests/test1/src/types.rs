pub fn run () {
    let s1 = "string01";
    let mut s2 = String::from("string02");
    println!("{:?}", (s1.len(), s2.len()));
    // println!("{:?}", (s1, s2, s1.len(), s2.len()));
    println!("{:?} {:?} {:?} {:?}", s1, s2, s1.len(), s2.len());

    println!("{}", s2);
    println!("{}", s2.len());
    println!("{}", s2.capacity());
    s2.push('-');

    println!("{}", s2);
    println!("{}", s2.len());
    println!("{}", s2.capacity());
    s2.push_str("000");

    println!("{}", s1);
}

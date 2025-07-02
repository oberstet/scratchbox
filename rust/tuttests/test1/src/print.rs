pub fn run() {
    println!("Hello from the print.rs file");

    println!("{} is from {}", "Brad", "Mass");

    println!(
        "{0} is from {1} and {0} likes to {2}",
        "Brad", "Mass", "code"
    );

    println!(
        "{name} likes to play {activity}",
        name = "John",
        activity = "Baseball"
    );
}

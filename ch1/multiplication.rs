fn multiplication(a: i64, b: i64) -> i64 {
    a * b // return a * b; 이렇게도 쓸 수 있다.
}

fn main() {
    let ex1 = multiplication(3, 5);
    println!("3+5={}", ex1);
    let ex2 = multiplication(8, 4);
    println!("8+4={}", ex2);
}
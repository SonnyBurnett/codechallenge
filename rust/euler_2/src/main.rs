fn main() {
    // the sum will be in the order of 10M so it's safe to use u32, which is in order of 4G
    let mut sum: u32 = 0;
    let mut fibs: [u32; 3] = [0, 1, 2];

    while fibs[2] < 4000000 {
        sum += fibs[2];
        fibs = next_3_fibonacci_steps(fibs)
    }

    println!("Sum of even fibonacci numbers < 4M: {}", sum);
}

// the sum of an uneven and even number is uneven, of two unevens even
// since we start with 1, 2 (uneven, even) we therefore know the following sets of 3 numbers in the fibsuence
// will always be (uneven, uneven, even)
fn next_3_fibonacci_steps(former: [u32; 3]) -> [u32; 3] {
    let next_0 = former[1] + former[2];
    let next_1 = former[2] + next_0;
    let next_2 = next_0 + next_1;
    [next_0, next_1, next_2]
}

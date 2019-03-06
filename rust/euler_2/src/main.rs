fn main() {
    // 4M is just within 2^32 (~4G), so it's safe to use u32
    let mut first: u32;
    let mut second: u32 = 1;
    let mut third: u32 = 2;
    let mut sum: u32 = 0;

    while third < 4000000 {
        // the sum of an uneven and even number is uneven, of two unevens even
        // since we start with 1, 2 (uneven, even) we therefore know the following sets of 3 numbers in the sequence
        // will always be (uneven, uneven, even)
        sum += third;

        first = second + third;
        second = third + first;
        third = first + second;
    }

    println!("Sum of even fibonacci numbers < 4M: {}", sum);
}

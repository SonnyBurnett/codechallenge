fn main() {
    // 4M is just within 2^32 (~4G), so it's safe to use u32
    let mut fibs: [u32; 3] = [0, 1, 2];
    let mut sum: u32 = 0;

    while fibs[2] < 4000000 {
        // the sum of an uneven and even number is uneven, of two unevens even
        // since we start with 1, 2 (uneven, even) we therefore know the following sets of 3 numbers in the fibsuence
        // will always be (uneven, uneven, even)
        sum += fibs[2];

        fibs[0] = fibs[1] + fibs[2];
        fibs[1] = fibs[2] + fibs[0];
        fibs[2] = fibs[0] + fibs[1];
    }

    println!("Sum of even fibonacci numbers < 4M: {}", sum);
}

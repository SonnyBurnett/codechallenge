# XOR decryption

## Problem analysis

First of all, I wondered if I needed to find the binary representiation of ASCII characters, given that XOR is an
operator in the domain of bits. After checking wikipedia on ASCII, it became apparent from the problem description that
a decimal encoding is used. Testing the out of the box XOR operator in Python made clear that we can simply use that:

    assert 65 ^ 42 == 107
    assert 107 ^ 42 == 65
    assert 65 ^ 107 == 42

Given is that `xor(x, y) = z IFF xor(z, y) = x`, where `y` is a character from the key. Since the key consists of three
characters only, we thus end up we three separate functions `xor_1`, `xor_2` and `xor_3` that bijectively map integers
onto one another. So, `xor_i(x) = z IFF xor_i(z) = x`. By cyclically slicing the input for every third character we
can find the bytes that each function has created.

Let's now use out knowledge of the english language, and analyse the frequency of letters in a random english text,
including the space character, and analyse the text. According to
[this source](https://web.archive.org/web/20170918020907/http://www.data-compression.com/english.html), the space is
the clear winner of occurence with 19.2%, nearly twice as much as the follow-up 'e' (10.4%). That is enough of a
difference that statistically a third of the given text should be enough to identify the space character in it's
encrypted forms. Then, we know two variables each of our three XOR statements (space is character 32), leading to a
crack of the three-letter password. Simple XOR operations then let us decode the entire message.

## Result of running the code

    An extract taken from the introduction of one of Euler's most celebrated papers, "De summis serierum reciprocarum"
    [On the sums of series of reciprocals]: I have recently found, quite unexpectedly, an elegant expression for the
    entire sum of this series 1 + 1/4 + 1/9 + 1/16 + etc., which depends on the quadrature of the circle, so that if
    the true sum of this series is obtained, from it at once the quadrature of the circle follows. Namely, I have found
    that the sum of this series is a sixth part of the square of the perimeter of the circle whose diameter is 1; or by
    putting the sum of this series equal to s, it has the ratio sqrt(6) multiplied by s to 1 of the perimeter to the
    diameter. I will soon show that the sum of this series to be approximately 1.644934066842264364; and from
    multiplying this number by six, and then taking the square root, the number 3.141592653589793238 is indeed
    produced, which expresses the perimeter of a circle whose diameter is 1. Following again the same steps by which I
    had arrived at this sum, I have discovered that the sum of the series 1 + 1/16 + 1/81 + 1/256 + 1/625 + etc. also
    depends on the quadrature of the circle. Namely, the sum of this multiplied by 90 gives the biquadrate (fourth
    power) of the circumference of the perimeter of a circle whose diameter is 1. And by similar reasoning I have
    likewise been able to determine the sums of the subsequent series in which the exponents are even numbers.

    The sum of the decoded ASCII codes is 129448

    python solution.py  0.04s user 0.01s system 93% cpu 0.052 total

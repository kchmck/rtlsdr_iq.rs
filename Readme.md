# rtlsdr\_iq – I/Q complex sample lookup table for RTL-SDR

[Documentation](https://docs.rs/rtlsdr_iq)

This crate provides a lookup table to map I/Q byte pairs from the RTL-SDR to complex,
floating-point samples.

## Example

```rust
use rtlsdr_iq::IQ;

// This is assuming little endian, where the Q byte is in the upper half of the word
// and the I byte is in the lower half.
let a = IQ[0x01_00u16];
let b = IQ[0x01_02u16];
let c = IQ[0x00_02u16];

assert!(a.re != b.re);
assert!(a.im == b.im);
assert!(b.re == c.re);
assert!(b.im != c.im);
```

## Usage

This [crate](https://crates.io/crates/rtlsdr_iq) can be used through cargo by adding it
as a dependency in `Cargo.toml`:

```toml
[dependencies]
rtlsdr_iq = "0.1.0"
```
and importing it in the crate root:

```rust
extern crate rtlsdr_iq;
```

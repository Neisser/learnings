//inline struct
struct Counter {
    items: Vec<i32>,
}

impl Counter {
    fn new(items: Vec<i32>) -> Counter {
        Counter { items: items }
    }
}

impl Iterator for Counter {
    type Item = i32;

    fn next(&mut self) -> Option<Self::Item> {
        if self.items.len() == 0 {
            return None;
        }

        let item: i32 = self.items[0];
        self.items.remove(0);
        Some(item)
    }
}

fn main() {
    println!("Hello, Iterators!");

    const ARRAY: [i32; 10] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    for i in ARRAY.iter() {
        println!("ARRAY = {}", i);
    }

    
    
    let mut vector: Vec<i32> = vec![1, 2, 3, 4, 5];
    
    vector.push(3);
    
    for i in vector.iter() {
        println!("vector = {}", i);
    }
    
    let arr: std::slice::Iter<'_, i32> = ARRAY.iter();
    
    let sum: i32 = arr.clone()
        .zip(vector.iter())
        .map(|(a, b)| a + b)
        .sum();

    println!("sum = {}", sum);

    let values = arr
        .zip(vector.iter())
        .map(|(a, b)| a + b);

    println!("values = {:?}", values);

    let counter: Counter = Counter::new(vec![1, 2, 3, 4, 5]);

    for i in counter {
        println!("counter = {}", i);
    }
}

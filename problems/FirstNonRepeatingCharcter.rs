fn fist_non_repeating_character(string: String) -> char {
    let mut found = HashMap::<char, i32>::new();
    let chars = string.chars().into_iter();
    for i in chars {
        if found.contains_key(&i) {
            found.insert(i, found.get(&i).unwrap() + 1);
        } else {
            found.insert(i, 1);
        }
    }
    for (key, value) in found.into_iter() {
        if value == 1 {
            return key
        }
    }
    return '_'
}
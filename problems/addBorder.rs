fn addBorder(picture: Vec<String>) -> Vec<String> {
    let mut output = vec![];
    let length = picture.len();
    let mut border = "*".repeat(picture[0].len() + 2).to_owned();
    output.push(format!("{}", border));
    for i in 0..length { 
        output.push(format!("*{}*", picture[i]));
    }
    output.push(format!("{}", border));
    println!("{:?}", output);
    output
}

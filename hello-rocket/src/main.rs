#[macro_use] extern crate rocket;

#[get("/")]
fn index() -> &'static str {
    "Hello, worlds!"
}

#[get("/greetings")]
fn greetings() -> &'static str {
    "Hello neisser saul!"
}

#[launch]
fn rocket() -> _ {
    rocket::build().mount("/", routes![index, greetings])
}

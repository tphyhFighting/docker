
Test case demonstrating that `!**...` directives do not work in `.dockerignore`.

To demonstrate, run

```bash
$ docker build -t dockerignore-test .

$ docker run --rm dockerignore-test
```

Notice that no `.py` files within directories are listed.


# Sempervivum

[Sempervivum](https://en.wikipedia.org/wiki/Sempervivum) is a genus of about 40 species of flowering plants in the family Crassulaceae, commonly known as houseleeks (dt. "Hauswurz"). The name Sempervivum has its origin in the Latin semper ("always") and vivus ("living").

The repository here however is about *two specific things*, mainly:

1. Use of **modern Python** development, language, packaging and documentation infrastructure and tools
2. **Simulation** of cellular growth in plants using [Gray-Scott Diffusion Model](https://groups.csail.mit.edu/mac/projects/amorphous/GrayScott/) based [Cellular Automata](https://biologicalmodeling.org/prologue/gray-scott) with Python

My interest in the latter arose since I was recently wondering why the Sempervivum plants on my terrasse grew nice rose flowers with *some* having 10 petals - and *others* 11 petals!

Turns out, the answer is not exactly obvious, surprising (I find) and (integer) numbers are core! Primes, Fibonacci, Non-Fibonacci and Lucas Sequences. That's when I woke up;)

Since I am a Math freak, but *also* a Pythonista, at some point it felt natural to try to *grow Sempervivum in my computer*, not only on my terrasse. And see if I can simulate growing a plant with say 10 petals.

On the other hand, since I am also currently bringing a number of Python OSS projects up to date with respect to modern tooling, and as part of that work I figured out a couple of neat tricks and experimented with best practices, which I want to preserve (I tend to forget a lot quickly again, hate having to rediscover/figure-out stuff), I thought:

Why not make the quick plant simulation hack into a nice demo *and* kind of memory aid at the same time, and also for others to check out or have fun!

So that's the story, and if you're with me and curious, let's stop blabbering and just do it! I show you, it's easy to try yourself, no worries.

`RETURN-REPEAT-LOOP`

## Usage

1. Start from a bare Unix (such as Linux, *BSD, macOS or Windows Subsystem for Linux (WSL)) with only a Shell and [curl](https://curl.se/).

2. Install [just](https://just.systems/):

```console
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to ${HOME}/.local/bin/
```

3. Install [uv](https://docs.astral.sh/uv/):

```console
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

Done. The rest "just" works!

To test:

```console
oberstet@amd-ryzen5:~/scm/oberstet/sempervivum$ just
Available recipes:
    default                       # list all recipes
    hello0 index_from index_until # basic test of recipe arguments
    hello1 index_from index_until # test of recipe arguments with shebang-based Python/uv recipe
    hello2 index_from index_until # test of recipe arguments with script-based Python/uv recipe
```



https://just.systems/man/en/shebang-recipes.html
https://just.systems/man/en/recipe-parameters.html
https://just.systems/man/en/script-recipes.html
https://just.systems/man/en/python-recipes-with-uv.html



JUST_TEMPDIR
JUST_UNSTABLE=1

just --fmt --unstable

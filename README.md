# Jobbr

By Jonathon Pemberton _<jonpemby@icloud.com>_

Search Google for job listings matching your criteria!

Backend script for a web app I'm writing. Eventually.

But you can use it now! Read on.

## Requirements

- Python 3+
- Google Custom Search Engine
- Google API Key

## Usage

### Help

Simply type:

```
jobbr.py --help
```

And Jobbr will output a help menu!

### Searches

Currently a search is basically just a raw Google query.

You can use the same boolean search syntax you're used to, which is great.

However, Jobbr intends to include some powerful abstractions over this to keep you from having to write a lot of parameters.

For now, type in your queries like this:

```
jobbr.py "data scientist"
```

You'll see results printed out to the screen in JSON format.

Jobbr will include paged (and human readable) output coming soon.

## Configuration

You'll need a CX key and a Google API key.

Jobbr recommends using environment variables to store these but if you need to you can pass them as parameters like so:

```
jobbr.py "data scientist" --api-key=$(API_KEY) --cx=$(CX_KEY)
```

Or, you can store them as environment variables:

```
JOBBR_API_KEY=[key]
JOBBR_CX_KEY=[id]
```

## License

Copyright © 2019 Jonathon Pemberton

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Issues

Please feel free to open an issue on this repo if you have any bugs.

PRs are welcome but are subject to the terms of the license.
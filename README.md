****[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/open-ortho/codes">
    <img src="https://raw.githubusercontent.com/open-ortho/dicom4ortho/master/images/open-ortho.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">codes</h3>

  <p align="center">
    A collection of codes and terms from various terminologies, specifically tailored for software development within the orthodontic domain.
    <br />
    <a href="https://open-ortho.github.io/codes/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/open-ortho/codes">View Demo</a>
    ·
    <a href="https://github.com/open-ortho/codes/issues">Report Bug</a>
    ·
    <a href="https://github.com/open-ortho/codes/issues">Request Feature</a>
  </p>
</p>

## About The Project

This project serves as a centralized repository for orthodontic software developers, offering a curated collection of essential codes required for implementing healthcare standards like DICOM or HL7. Navigating through various terminologies to find the right codes can be challenging. Our project aims to simplify this process by providing a go-to source for these codes, readily available in JSON and CSV formats. Users can access these directly through GitHub releases or utilize them as a Python package on PyPI.

## Using The Codes

### Python

If you want to use the codes directly in your Python project:

    pip install open-ortho-codes

Then

    from ortho_codes import hl7 as codes_hl7

    print(f"{codes_hl7.orthodontic.system}")
    print(codes_hl7.orthodontic.code)
    print(codes_hl7.orthodontic.display)

Convert codes to JSON

    from ortho_codes import hl7 as codes_hl7

    print(f"{codes_hl7.orthodontic.to_json()}")

### JSON

Just point your code to any of the following:


## Releases

- Each new release must be git tagged with v*.*.*. This triggers the Github actions to publish to PyPi and release in GitHub releases.
- 
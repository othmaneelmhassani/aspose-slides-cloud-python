![](https://img.shields.io/badge/api-v3.0-lightgrey) ![PyPI](https://img.shields.io/pypi/v/asposeslidescloud) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/asposeslidescloud) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/asposeslidescloud) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/asposeslidescloud) [![GitHub license](https://img.shields.io/github/license/aspose-slides-cloud/aspose-slides-cloud-python)](https://github.com/aspose-slides-cloud/aspose-slides-cloud-python/blob/master/LICENSE)
# Aspose.Slides Cloud SDK for Python
This repository contains Aspose.Slides Cloud SDK for Python source code. This SDK allows you to work with Aspose.Slides Cloud REST APIs in your Python applications.

## Key Features
* Conversion between various document-related formats (20+ formats supported), including PDF<->PowerPoint conversion
* Download slides and shapes in various formats, including PDF and SVG
* Merge and split PowerPoint presentations
* Access PowerPoint presentation metadata and statistics
* Find and replace
* Full read & write access to Document Object Model, including slides, shapes, paragraphs, portions and many others
* Support of Aspose.Storage API

## Licensing
All Aspose.Slides Cloud SDKs are licensed under MIT License.

## How to use the SDK?
The complete source code is available in this repository folder. You can either directly use it in your project via source code or get [PuPi module](https://pypi.org/project/asposeslidescloud) (recommended).

## Prerequisites
To use Aspose Slides Cloud SDK for Python you need to register an account with [Aspose Cloud](https://www.aspose.cloud/) and lookup/create App Key and SID at [Cloud Dashboard](https://dashboard.aspose.cloud/#/apps). There is free quota available. For more details, see [Aspose Cloud Pricing](https://purchase.aspose.cloud/pricing).

### Installation

```sh
python -m pip install asposeslidescloud
```

### Sample usage

The example code below converts a PowerPoint document to PDF format using asposeslidescloud library:
```python
	import asposeslidescloud

	from asposeslidescloud.configuration import Configuration
	from asposeslidescloud.apis.slides_api import SlidesApi
	from asposeslidescloud.models.export_format import ExportFormat
	from asposeslidescloud.models.requests.slides_api_requests import PostSlidesConvertRequest

	configuration = Configuration()
	configuration.app_sid = 'MyClientId'
	configuration.app_key = 'MyClientSecret'
	api = SlidesApi(configuration)

	with open("MyPresentation.pptx", 'rb') as f:
		document = f.read()

	request = PostSlidesConvertRequest(ExportFormat.PDF, document)
	response = api.post_slides_convert(request)
	print('My PDF was saved to ' + response)
```

You can check more [Examples](Examples) of using the SDK.

## Aspose.Slides Cloud SDKs in Popular Languages

| .NET | Java | PHP | Python | Ruby | Node.js | Android | Swift|Perl|Go|
|---|---|---|---|---|---|---|--|--|--|
| [GitHub](https://github.com/aspose-slides-cloud/aspose-slides-cloud-dotnet) | [GitHub](https://github.com/aspose-slides-cloud/aspose-slides-cloud-java) | [GitHub](https://github.com/aspose-slides-cloud/aspose-slides-cloud-php) | [GitHub](https://github.com/aspose-slides-cloud/aspose-slides-cloud-python) | [GitHub](https://github.com/aspose-slides-cloud/aspose-slides-cloud-ruby)  | [GitHub](https://github.com/aspose-slides-cloud/aspose-slides-cloud-nodejs) | [GitHub](https://github.com/aspose-slides-cloud/aspose-slides-cloud-android) | [GitHub](https://github.com/aspose-slides-cloud/aspose-slides-cloud-swift)|[GitHub](https://github.com/aspose-slides-cloud/aspose-slides-cloud-perl) |[GitHub](https://github.com/aspose-slides-cloud/aspose-slides-cloud-go) |
| [NuGet](https://www.nuget.org/packages/Aspose.slides-Cloud/) | [Maven](https://repository.aspose.cloud/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-slides-cloud) | [Composer](https://packagist.org/packages/aspose/slides-sdk-php) | [PIP](https://pypi.org/project/asposeslidescloud/) | [GEM](https://rubygems.org/gems/aspose_slides_cloud)  | [NPM](https://www.npmjs.com/package/asposeslidescloud) | [Maven](https://repository.aspose.cloud/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-slides-cloud) | [Cocoapods](https://cocoapods.org/pods/AsposeslidesCloud)|[Meta Cpan](https://metacpan.org/release/AsposeSlidesCloud-SlidesApi) | [Go.Dev](https://pkg.go.dev/github.com/aspose-slides-cloud/aspose-slides-cloud-go/) | 

[Product Page](https://products.aspose.cloud/slides/python) | [Documentation](https://docs.aspose.cloud/display/slidescloud/Home) | [API Reference](https://apireference.aspose.cloud/slides/) | [Code Samples](https://github.com/aspose-slides-cloud/aspose-slides-cloud-python) | [Blog](https://blog.aspose.cloud/category/slides/) | [Free Support](https://forum.aspose.cloud/c/slides) | [Free Trial](https://dashboard.aspose.cloud/#/apps)

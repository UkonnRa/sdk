# ory_kratos_client
Welcome to the ORY Kratos HTTP API documentation!

This Dart package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v0.0.0
- Build package: org.openapitools.codegen.languages.DartClientCodegen

## Requirements

Dart 2.0 or later

## Installation & Usage

### Github
If this Dart package is published to Github, add the following dependency to your pubspec.yaml
```
dependencies:
  ory_kratos_client:
    git: https://github.com/ory/sdk.git
```

### Local
To use the package in your local drive, add the following dependency to your pubspec.yaml
```
dependencies:
  ory_kratos_client:
    path: /path/to/ory_kratos_client
```

## Tests

TODO

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```dart
import 'package:ory_kratos_client/api.dart';


final api_instance = HealthApi();

try {
    final result = api_instance.isInstanceAlive();
    print(result);
} catch (e) {
    print('Exception when calling HealthApi->isInstanceAlive: $e\n');
}

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*HealthApi* | [**isInstanceAlive**](doc//HealthApi.md#isinstancealive) | **GET** /health/alive | Check alive status
*HealthApi* | [**isInstanceReady**](doc//HealthApi.md#isinstanceready) | **GET** /health/ready | Check readiness status
*PublicApi* | [**completeProfileManagementFlow**](doc//PublicApi.md#completeprofilemanagementflow) | **POST** /profiles | Complete Profile Management Flow
*PublicApi* | [**getLoginRequest**](doc//PublicApi.md#getloginrequest) | **GET** /auth/browser/requests/login | Get Login Request
*PublicApi* | [**getProfileManagementRequest**](doc//PublicApi.md#getprofilemanagementrequest) | **GET** /profiles/requests | Get Profile Management Request (via cookie)
*PublicApi* | [**getRegistrationRequest**](doc//PublicApi.md#getregistrationrequest) | **GET** /auth/browser/requests/registration | Get Registration Request
*PublicApi* | [**initializeLoginFlow**](doc//PublicApi.md#initializeloginflow) | **GET** /auth/browser/login | Initialize a Login Flow
*PublicApi* | [**initializeProfileManagementFlow**](doc//PublicApi.md#initializeprofilemanagementflow) | **GET** /profiles | Initialize Profile Management Flow
*PublicApi* | [**initializeRegistrationFlow**](doc//PublicApi.md#initializeregistrationflow) | **GET** /auth/browser/registration | Initialize a Registration Flow
*VersionApi* | [**getVersion**](doc//VersionApi.md#getversion) | **GET** /version | Get service version


## Documentation For Models

 - [Error](doc//Error.md)
 - [Form](doc//Form.md)
 - [FormField](doc//FormField.md)
 - [GenericError](doc//GenericError.md)
 - [HealthNotReadyStatus](doc//HealthNotReadyStatus.md)
 - [HealthStatus](doc//HealthStatus.md)
 - [Identity](doc//Identity.md)
 - [LoginRequest](doc//LoginRequest.md)
 - [LoginRequestMethod](doc//LoginRequestMethod.md)
 - [LoginRequestMethodConfig](doc//LoginRequestMethodConfig.md)
 - [OidcStrategyCredentialsConfig](doc//OidcStrategyCredentialsConfig.md)
 - [OidcStrategyRequestMethod](doc//OidcStrategyRequestMethod.md)
 - [ProfileManagementRequest](doc//ProfileManagementRequest.md)
 - [RegistrationRequest](doc//RegistrationRequest.md)
 - [RegistrationRequestMethod](doc//RegistrationRequestMethod.md)
 - [RegistrationRequestMethodConfig](doc//RegistrationRequestMethodConfig.md)
 - [Version](doc//Version.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author





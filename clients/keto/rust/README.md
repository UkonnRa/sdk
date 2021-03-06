# Rust API client for ory-keto-client

Ory Keto is a cloud native access control server providing best-practice patterns (RBAC, ABAC, ACL, AWS IAM Policies, Kubernetes Roles, ...) via REST APIs.

## Overview

This API client was generated by the [OpenAPI Generator](https://openapi-generator.tech) project.  By using the [openapi-spec](https://openapis.org) from a remote server, you can easily generate an API client.

- API version: v0.0.0-alpha.58
- Package version: v0.0.0-alpha.58
- Build package: org.openapitools.codegen.languages.RustClientCodegen
For more information, please visit [https://www.ory.sh](https://www.ory.sh)

## Installation

Put the package under your project folder and add the following to `Cargo.toml` under `[dependencies]`:

```
    openapi = { path = "./generated" }
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*EnginesApi* | [**add_ory_access_control_policy_role_members**](docs/EnginesApi.md#add_ory_access_control_policy_role_members) | **put** /engines/acp/ory/{flavor}/roles/{id}/members | Add a member to an ORY Access Control Policy Role
*EnginesApi* | [**delete_ory_access_control_policy**](docs/EnginesApi.md#delete_ory_access_control_policy) | **delete** /engines/acp/ory/{flavor}/policies/{id} | 
*EnginesApi* | [**delete_ory_access_control_policy_role**](docs/EnginesApi.md#delete_ory_access_control_policy_role) | **delete** /engines/acp/ory/{flavor}/roles/{id} | Delete an ORY Access Control Policy Role
*EnginesApi* | [**do_ory_access_control_policies_allow**](docs/EnginesApi.md#do_ory_access_control_policies_allow) | **post** /engines/acp/ory/{flavor}/allowed | Check if a request is allowed
*EnginesApi* | [**get_ory_access_control_policy**](docs/EnginesApi.md#get_ory_access_control_policy) | **get** /engines/acp/ory/{flavor}/policies/{id} | 
*EnginesApi* | [**get_ory_access_control_policy_role**](docs/EnginesApi.md#get_ory_access_control_policy_role) | **get** /engines/acp/ory/{flavor}/roles/{id} | Get an ORY Access Control Policy Role
*EnginesApi* | [**list_ory_access_control_policies**](docs/EnginesApi.md#list_ory_access_control_policies) | **get** /engines/acp/ory/{flavor}/policies | 
*EnginesApi* | [**list_ory_access_control_policy_roles**](docs/EnginesApi.md#list_ory_access_control_policy_roles) | **get** /engines/acp/ory/{flavor}/roles | List ORY Access Control Policy Roles
*EnginesApi* | [**remove_ory_access_control_policy_role_members**](docs/EnginesApi.md#remove_ory_access_control_policy_role_members) | **delete** /engines/acp/ory/{flavor}/roles/{id}/members/{member} | Remove a member from an ORY Access Control Policy Role
*EnginesApi* | [**upsert_ory_access_control_policy**](docs/EnginesApi.md#upsert_ory_access_control_policy) | **put** /engines/acp/ory/{flavor}/policies | 
*EnginesApi* | [**upsert_ory_access_control_policy_role**](docs/EnginesApi.md#upsert_ory_access_control_policy_role) | **put** /engines/acp/ory/{flavor}/roles | Upsert an ORY Access Control Policy Role
*HealthApi* | [**is_instance_alive**](docs/HealthApi.md#is_instance_alive) | **get** /health/alive | Check alive status
*HealthApi* | [**is_instance_ready**](docs/HealthApi.md#is_instance_ready) | **get** /health/ready | Check readiness status
*VersionApi* | [**get_version**](docs/VersionApi.md#get_version) | **get** /version | Get service version


## Documentation For Models

 - [AddOryAccessControlPolicyRoleMembersBody](docs/AddOryAccessControlPolicyRoleMembersBody.md)
 - [AuthorizationResult](docs/AuthorizationResult.md)
 - [HealthNotReadyStatus](docs/HealthNotReadyStatus.md)
 - [HealthStatus](docs/HealthStatus.md)
 - [InlineResponse500](docs/InlineResponse500.md)
 - [OryAccessControlPolicy](docs/OryAccessControlPolicy.md)
 - [OryAccessControlPolicyAllowedInput](docs/OryAccessControlPolicyAllowedInput.md)
 - [OryAccessControlPolicyRole](docs/OryAccessControlPolicyRole.md)
 - [Version](docs/Version.md)


To get access to the crate's generated documentation, use:

```
cargo doc --open
```

## Author

hi@ory.sh


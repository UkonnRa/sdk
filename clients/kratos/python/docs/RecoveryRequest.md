# RecoveryRequest

This request is used when an identity wants to recover their account.  We recommend reading the [Account Recovery Documentation](../self-service/flows/password-reset-account-recovery)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **str** | Active, if set, contains the registration method that is being used. It is initially not set. | [optional] 
**expires_at** | **datetime** | ExpiresAt is the time (UTC) when the request expires. If the user still wishes to update the setting, a new request has to be initiated. | 
**id** | **str** |  | 
**issued_at** | **datetime** | IssuedAt is the time (UTC) when the request occurred. | 
**messages** | [**list[Message]**](Message.md) |  | [optional] 
**methods** | [**dict(str, RecoveryRequestMethod)**](RecoveryRequestMethod.md) | Methods contains context for all account recovery methods. If a registration request has been processed, but for example the password is incorrect, this will contain error messages. | 
**request_url** | **str** | RequestURL is the initial URL that was requested from ORY Kratos. It can be used to forward information contained in the URL&#39;s path or query for example. | 
**state** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# coding: utf-8

"""
    ORY Hydra

    Welcome to the ORY Hydra HTTP API documentation. You will find documentation for all HTTP APIs here.  # noqa: E501

    The version of the OpenAPI document: v1.9.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ory_hydra_client.configuration import Configuration


class UserinfoResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'birthdate': 'str',
        'email': 'str',
        'email_verified': 'bool',
        'family_name': 'str',
        'gender': 'str',
        'given_name': 'str',
        'locale': 'str',
        'middle_name': 'str',
        'name': 'str',
        'nickname': 'str',
        'phone_number': 'str',
        'phone_number_verified': 'bool',
        'picture': 'str',
        'preferred_username': 'str',
        'profile': 'str',
        'sub': 'str',
        'updated_at': 'int',
        'website': 'str',
        'zoneinfo': 'str'
    }

    attribute_map = {
        'birthdate': 'birthdate',
        'email': 'email',
        'email_verified': 'email_verified',
        'family_name': 'family_name',
        'gender': 'gender',
        'given_name': 'given_name',
        'locale': 'locale',
        'middle_name': 'middle_name',
        'name': 'name',
        'nickname': 'nickname',
        'phone_number': 'phone_number',
        'phone_number_verified': 'phone_number_verified',
        'picture': 'picture',
        'preferred_username': 'preferred_username',
        'profile': 'profile',
        'sub': 'sub',
        'updated_at': 'updated_at',
        'website': 'website',
        'zoneinfo': 'zoneinfo'
    }

    def __init__(self, birthdate=None, email=None, email_verified=None, family_name=None, gender=None, given_name=None, locale=None, middle_name=None, name=None, nickname=None, phone_number=None, phone_number_verified=None, picture=None, preferred_username=None, profile=None, sub=None, updated_at=None, website=None, zoneinfo=None, local_vars_configuration=None):  # noqa: E501
        """UserinfoResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._birthdate = None
        self._email = None
        self._email_verified = None
        self._family_name = None
        self._gender = None
        self._given_name = None
        self._locale = None
        self._middle_name = None
        self._name = None
        self._nickname = None
        self._phone_number = None
        self._phone_number_verified = None
        self._picture = None
        self._preferred_username = None
        self._profile = None
        self._sub = None
        self._updated_at = None
        self._website = None
        self._zoneinfo = None
        self.discriminator = None

        if birthdate is not None:
            self.birthdate = birthdate
        if email is not None:
            self.email = email
        if email_verified is not None:
            self.email_verified = email_verified
        if family_name is not None:
            self.family_name = family_name
        if gender is not None:
            self.gender = gender
        if given_name is not None:
            self.given_name = given_name
        if locale is not None:
            self.locale = locale
        if middle_name is not None:
            self.middle_name = middle_name
        if name is not None:
            self.name = name
        if nickname is not None:
            self.nickname = nickname
        if phone_number is not None:
            self.phone_number = phone_number
        if phone_number_verified is not None:
            self.phone_number_verified = phone_number_verified
        if picture is not None:
            self.picture = picture
        if preferred_username is not None:
            self.preferred_username = preferred_username
        if profile is not None:
            self.profile = profile
        if sub is not None:
            self.sub = sub
        if updated_at is not None:
            self.updated_at = updated_at
        if website is not None:
            self.website = website
        if zoneinfo is not None:
            self.zoneinfo = zoneinfo

    @property
    def birthdate(self):
        """Gets the birthdate of this UserinfoResponse.  # noqa: E501

        End-User's birthday, represented as an ISO 8601:2004 [ISO8601‑2004] YYYY-MM-DD format. The year MAY be 0000, indicating that it is omitted. To represent only the year, YYYY format is allowed. Note that depending on the underlying platform's date related function, providing just year can result in varying month and day, so the implementers need to take this factor into account to correctly process the dates.  # noqa: E501

        :return: The birthdate of this UserinfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._birthdate

    @birthdate.setter
    def birthdate(self, birthdate):
        """Sets the birthdate of this UserinfoResponse.

        End-User's birthday, represented as an ISO 8601:2004 [ISO8601‑2004] YYYY-MM-DD format. The year MAY be 0000, indicating that it is omitted. To represent only the year, YYYY format is allowed. Note that depending on the underlying platform's date related function, providing just year can result in varying month and day, so the implementers need to take this factor into account to correctly process the dates.  # noqa: E501

        :param birthdate: The birthdate of this UserinfoResponse.  # noqa: E501
        :type: str
        """

        self._birthdate = birthdate

    @property
    def email(self):
        """Gets the email of this UserinfoResponse.  # noqa: E501

        End-User's preferred e-mail address. Its value MUST conform to the RFC 5322 [RFC5322] addr-spec syntax. The RP MUST NOT rely upon this value being unique, as discussed in Section 5.7.  # noqa: E501

        :return: The email of this UserinfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserinfoResponse.

        End-User's preferred e-mail address. Its value MUST conform to the RFC 5322 [RFC5322] addr-spec syntax. The RP MUST NOT rely upon this value being unique, as discussed in Section 5.7.  # noqa: E501

        :param email: The email of this UserinfoResponse.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def email_verified(self):
        """Gets the email_verified of this UserinfoResponse.  # noqa: E501

        True if the End-User's e-mail address has been verified; otherwise false. When this Claim Value is true, this means that the OP took affirmative steps to ensure that this e-mail address was controlled by the End-User at the time the verification was performed. The means by which an e-mail address is verified is context-specific, and dependent upon the trust framework or contractual agreements within which the parties are operating.  # noqa: E501

        :return: The email_verified of this UserinfoResponse.  # noqa: E501
        :rtype: bool
        """
        return self._email_verified

    @email_verified.setter
    def email_verified(self, email_verified):
        """Sets the email_verified of this UserinfoResponse.

        True if the End-User's e-mail address has been verified; otherwise false. When this Claim Value is true, this means that the OP took affirmative steps to ensure that this e-mail address was controlled by the End-User at the time the verification was performed. The means by which an e-mail address is verified is context-specific, and dependent upon the trust framework or contractual agreements within which the parties are operating.  # noqa: E501

        :param email_verified: The email_verified of this UserinfoResponse.  # noqa: E501
        :type: bool
        """

        self._email_verified = email_verified

    @property
    def family_name(self):
        """Gets the family_name of this UserinfoResponse.  # noqa: E501

        Surname(s) or last name(s) of the End-User. Note that in some cultures, people can have multiple family names or no family name; all can be present, with the names being separated by space characters.  # noqa: E501

        :return: The family_name of this UserinfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._family_name

    @family_name.setter
    def family_name(self, family_name):
        """Sets the family_name of this UserinfoResponse.

        Surname(s) or last name(s) of the End-User. Note that in some cultures, people can have multiple family names or no family name; all can be present, with the names being separated by space characters.  # noqa: E501

        :param family_name: The family_name of this UserinfoResponse.  # noqa: E501
        :type: str
        """

        self._family_name = family_name

    @property
    def gender(self):
        """Gets the gender of this UserinfoResponse.  # noqa: E501

        End-User's gender. Values defined by this specification are female and male. Other values MAY be used when neither of the defined values are applicable.  # noqa: E501

        :return: The gender of this UserinfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this UserinfoResponse.

        End-User's gender. Values defined by this specification are female and male. Other values MAY be used when neither of the defined values are applicable.  # noqa: E501

        :param gender: The gender of this UserinfoResponse.  # noqa: E501
        :type: str
        """

        self._gender = gender

    @property
    def given_name(self):
        """Gets the given_name of this UserinfoResponse.  # noqa: E501

        Given name(s) or first name(s) of the End-User. Note that in some cultures, people can have multiple given names; all can be present, with the names being separated by space characters.  # noqa: E501

        :return: The given_name of this UserinfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """Sets the given_name of this UserinfoResponse.

        Given name(s) or first name(s) of the End-User. Note that in some cultures, people can have multiple given names; all can be present, with the names being separated by space characters.  # noqa: E501

        :param given_name: The given_name of this UserinfoResponse.  # noqa: E501
        :type: str
        """

        self._given_name = given_name

    @property
    def locale(self):
        """Gets the locale of this UserinfoResponse.  # noqa: E501

        End-User's locale, represented as a BCP47 [RFC5646] language tag. This is typically an ISO 639-1 Alpha-2 [ISO639‑1] language code in lowercase and an ISO 3166-1 Alpha-2 [ISO3166‑1] country code in uppercase, separated by a dash. For example, en-US or fr-CA. As a compatibility note, some implementations have used an underscore as the separator rather than a dash, for example, en_US; Relying Parties MAY choose to accept this locale syntax as well.  # noqa: E501

        :return: The locale of this UserinfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this UserinfoResponse.

        End-User's locale, represented as a BCP47 [RFC5646] language tag. This is typically an ISO 639-1 Alpha-2 [ISO639‑1] language code in lowercase and an ISO 3166-1 Alpha-2 [ISO3166‑1] country code in uppercase, separated by a dash. For example, en-US or fr-CA. As a compatibility note, some implementations have used an underscore as the separator rather than a dash, for example, en_US; Relying Parties MAY choose to accept this locale syntax as well.  # noqa: E501

        :param locale: The locale of this UserinfoResponse.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def middle_name(self):
        """Gets the middle_name of this UserinfoResponse.  # noqa: E501

        Middle name(s) of the End-User. Note that in some cultures, people can have multiple middle names; all can be present, with the names being separated by space characters. Also note that in some cultures, middle names are not used.  # noqa: E501

        :return: The middle_name of this UserinfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this UserinfoResponse.

        Middle name(s) of the End-User. Note that in some cultures, people can have multiple middle names; all can be present, with the names being separated by space characters. Also note that in some cultures, middle names are not used.  # noqa: E501

        :param middle_name: The middle_name of this UserinfoResponse.  # noqa: E501
        :type: str
        """

        self._middle_name = middle_name

    @property
    def name(self):
        """Gets the name of this UserinfoResponse.  # noqa: E501

        End-User's full name in displayable form including all name parts, possibly including titles and suffixes, ordered according to the End-User's locale and preferences.  # noqa: E501

        :return: The name of this UserinfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserinfoResponse.

        End-User's full name in displayable form including all name parts, possibly including titles and suffixes, ordered according to the End-User's locale and preferences.  # noqa: E501

        :param name: The name of this UserinfoResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def nickname(self):
        """Gets the nickname of this UserinfoResponse.  # noqa: E501

        Casual name of the End-User that may or may not be the same as the given_name. For instance, a nickname value of Mike might be returned alongside a given_name value of Michael.  # noqa: E501

        :return: The nickname of this UserinfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """Sets the nickname of this UserinfoResponse.

        Casual name of the End-User that may or may not be the same as the given_name. For instance, a nickname value of Mike might be returned alongside a given_name value of Michael.  # noqa: E501

        :param nickname: The nickname of this UserinfoResponse.  # noqa: E501
        :type: str
        """

        self._nickname = nickname

    @property
    def phone_number(self):
        """Gets the phone_number of this UserinfoResponse.  # noqa: E501

        End-User's preferred telephone number. E.164 [E.164] is RECOMMENDED as the format of this Claim, for example, +1 (425) 555-1212 or +56 (2) 687 2400. If the phone number contains an extension, it is RECOMMENDED that the extension be represented using the RFC 3966 [RFC3966] extension syntax, for example, +1 (604) 555-1234;ext=5678.  # noqa: E501

        :return: The phone_number of this UserinfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this UserinfoResponse.

        End-User's preferred telephone number. E.164 [E.164] is RECOMMENDED as the format of this Claim, for example, +1 (425) 555-1212 or +56 (2) 687 2400. If the phone number contains an extension, it is RECOMMENDED that the extension be represented using the RFC 3966 [RFC3966] extension syntax, for example, +1 (604) 555-1234;ext=5678.  # noqa: E501

        :param phone_number: The phone_number of this UserinfoResponse.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def phone_number_verified(self):
        """Gets the phone_number_verified of this UserinfoResponse.  # noqa: E501

        True if the End-User's phone number has been verified; otherwise false. When this Claim Value is true, this means that the OP took affirmative steps to ensure that this phone number was controlled by the End-User at the time the verification was performed. The means by which a phone number is verified is context-specific, and dependent upon the trust framework or contractual agreements within which the parties are operating. When true, the phone_number Claim MUST be in E.164 format and any extensions MUST be represented in RFC 3966 format.  # noqa: E501

        :return: The phone_number_verified of this UserinfoResponse.  # noqa: E501
        :rtype: bool
        """
        return self._phone_number_verified

    @phone_number_verified.setter
    def phone_number_verified(self, phone_number_verified):
        """Sets the phone_number_verified of this UserinfoResponse.

        True if the End-User's phone number has been verified; otherwise false. When this Claim Value is true, this means that the OP took affirmative steps to ensure that this phone number was controlled by the End-User at the time the verification was performed. The means by which a phone number is verified is context-specific, and dependent upon the trust framework or contractual agreements within which the parties are operating. When true, the phone_number Claim MUST be in E.164 format and any extensions MUST be represented in RFC 3966 format.  # noqa: E501

        :param phone_number_verified: The phone_number_verified of this UserinfoResponse.  # noqa: E501
        :type: bool
        """

        self._phone_number_verified = phone_number_verified

    @property
    def picture(self):
        """Gets the picture of this UserinfoResponse.  # noqa: E501

        URL of the End-User's profile picture. This URL MUST refer to an image file (for example, a PNG, JPEG, or GIF image file), rather than to a Web page containing an image. Note that this URL SHOULD specifically reference a profile photo of the End-User suitable for displaying when describing the End-User, rather than an arbitrary photo taken by the End-User.  # noqa: E501

        :return: The picture of this UserinfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._picture

    @picture.setter
    def picture(self, picture):
        """Sets the picture of this UserinfoResponse.

        URL of the End-User's profile picture. This URL MUST refer to an image file (for example, a PNG, JPEG, or GIF image file), rather than to a Web page containing an image. Note that this URL SHOULD specifically reference a profile photo of the End-User suitable for displaying when describing the End-User, rather than an arbitrary photo taken by the End-User.  # noqa: E501

        :param picture: The picture of this UserinfoResponse.  # noqa: E501
        :type: str
        """

        self._picture = picture

    @property
    def preferred_username(self):
        """Gets the preferred_username of this UserinfoResponse.  # noqa: E501

        Non-unique shorthand name by which the End-User wishes to be referred to at the RP, such as janedoe or j.doe. This value MAY be any valid JSON string including special characters such as @, /, or whitespace.  # noqa: E501

        :return: The preferred_username of this UserinfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._preferred_username

    @preferred_username.setter
    def preferred_username(self, preferred_username):
        """Sets the preferred_username of this UserinfoResponse.

        Non-unique shorthand name by which the End-User wishes to be referred to at the RP, such as janedoe or j.doe. This value MAY be any valid JSON string including special characters such as @, /, or whitespace.  # noqa: E501

        :param preferred_username: The preferred_username of this UserinfoResponse.  # noqa: E501
        :type: str
        """

        self._preferred_username = preferred_username

    @property
    def profile(self):
        """Gets the profile of this UserinfoResponse.  # noqa: E501

        URL of the End-User's profile page. The contents of this Web page SHOULD be about the End-User.  # noqa: E501

        :return: The profile of this UserinfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this UserinfoResponse.

        URL of the End-User's profile page. The contents of this Web page SHOULD be about the End-User.  # noqa: E501

        :param profile: The profile of this UserinfoResponse.  # noqa: E501
        :type: str
        """

        self._profile = profile

    @property
    def sub(self):
        """Gets the sub of this UserinfoResponse.  # noqa: E501

        Subject - Identifier for the End-User at the IssuerURL.  # noqa: E501

        :return: The sub of this UserinfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._sub

    @sub.setter
    def sub(self, sub):
        """Sets the sub of this UserinfoResponse.

        Subject - Identifier for the End-User at the IssuerURL.  # noqa: E501

        :param sub: The sub of this UserinfoResponse.  # noqa: E501
        :type: str
        """

        self._sub = sub

    @property
    def updated_at(self):
        """Gets the updated_at of this UserinfoResponse.  # noqa: E501

        Time the End-User's information was last updated. Its value is a JSON number representing the number of seconds from 1970-01-01T0:0:0Z as measured in UTC until the date/time.  # noqa: E501

        :return: The updated_at of this UserinfoResponse.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this UserinfoResponse.

        Time the End-User's information was last updated. Its value is a JSON number representing the number of seconds from 1970-01-01T0:0:0Z as measured in UTC until the date/time.  # noqa: E501

        :param updated_at: The updated_at of this UserinfoResponse.  # noqa: E501
        :type: int
        """

        self._updated_at = updated_at

    @property
    def website(self):
        """Gets the website of this UserinfoResponse.  # noqa: E501

        URL of the End-User's Web page or blog. This Web page SHOULD contain information published by the End-User or an organization that the End-User is affiliated with.  # noqa: E501

        :return: The website of this UserinfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this UserinfoResponse.

        URL of the End-User's Web page or blog. This Web page SHOULD contain information published by the End-User or an organization that the End-User is affiliated with.  # noqa: E501

        :param website: The website of this UserinfoResponse.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def zoneinfo(self):
        """Gets the zoneinfo of this UserinfoResponse.  # noqa: E501

        String from zoneinfo [zoneinfo] time zone database representing the End-User's time zone. For example, Europe/Paris or America/Los_Angeles.  # noqa: E501

        :return: The zoneinfo of this UserinfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._zoneinfo

    @zoneinfo.setter
    def zoneinfo(self, zoneinfo):
        """Sets the zoneinfo of this UserinfoResponse.

        String from zoneinfo [zoneinfo] time zone database representing the End-User's time zone. For example, Europe/Paris or America/Los_Angeles.  # noqa: E501

        :param zoneinfo: The zoneinfo of this UserinfoResponse.  # noqa: E501
        :type: str
        """

        self._zoneinfo = zoneinfo

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserinfoResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserinfoResponse):
            return True

        return self.to_dict() != other.to_dict()

=begin
#ORY Hydra

#Welcome to the ORY Hydra HTTP API documentation. You will find documentation for all HTTP APIs here.

The version of the OpenAPI document: latest

Generated by: https://openapi-generator.tech
OpenAPI Generator version: 4.2.3

=end

require 'date'

module OryHydraClient
  # PreviousConsentSession PreviousConsentSession PreviousConsentSession PreviousConsentSession PreviousConsentSession PreviousConsentSession PreviousConsentSession PreviousConsentSession PreviousConsentSession PreviousConsentSession PreviousConsentSession The response used to return used consent requests same as HandledLoginRequest, just with consent_request exposed as json
  class PreviousConsentSession
    attr_accessor :consent_request

    # GrantedAudience sets the audience the user authorized the client to use. Should be a subset of `requested_access_token_audience`.
    attr_accessor :grant_access_token_audience

    # GrantScope sets the scope the user authorized the client to use. Should be a subset of `requested_scope`
    attr_accessor :grant_scope

    # handled at Format: date-time Format: date-time Format: date-time Format: date-time Format: date-time Format: date-time Format: date-time Format: date-time Format: date-time Format: date-time Format: date-time
    attr_accessor :handled_at

    # Remember, if set to true, tells ORY Hydra to remember this consent authorization and reuse it if the same client asks the same user for the same, or a subset of, scope.
    attr_accessor :remember

    # RememberFor sets how long the consent authorization should be remembered for in seconds. If set to `0`, the authorization will be remembered indefinitely.
    attr_accessor :remember_for

    attr_accessor :session

    # Attribute mapping from ruby-style variable name to JSON key.
    def self.attribute_map
      {
        :'consent_request' => :'consent_request',
        :'grant_access_token_audience' => :'grant_access_token_audience',
        :'grant_scope' => :'grant_scope',
        :'handled_at' => :'handled_at',
        :'remember' => :'remember',
        :'remember_for' => :'remember_for',
        :'session' => :'session'
      }
    end

    # Attribute type mapping.
    def self.openapi_types
      {
        :'consent_request' => :'ConsentRequest',
        :'grant_access_token_audience' => :'Array<String>',
        :'grant_scope' => :'Array<String>',
        :'handled_at' => :'DateTime',
        :'remember' => :'Boolean',
        :'remember_for' => :'Integer',
        :'session' => :'ConsentRequestSession'
      }
    end

    # List of attributes with nullable: true
    def self.openapi_nullable
      Set.new([
      ])
    end

    # Initializes the object
    # @param [Hash] attributes Model attributes in the form of hash
    def initialize(attributes = {})
      if (!attributes.is_a?(Hash))
        fail ArgumentError, "The input argument (attributes) must be a hash in `OryHydraClient::PreviousConsentSession` initialize method"
      end

      # check to see if the attribute exists and convert string to symbol for hash key
      attributes = attributes.each_with_object({}) { |(k, v), h|
        if (!self.class.attribute_map.key?(k.to_sym))
          fail ArgumentError, "`#{k}` is not a valid attribute in `OryHydraClient::PreviousConsentSession`. Please check the name to make sure it's valid. List of attributes: " + self.class.attribute_map.keys.inspect
        end
        h[k.to_sym] = v
      }

      if attributes.key?(:'consent_request')
        self.consent_request = attributes[:'consent_request']
      end

      if attributes.key?(:'grant_access_token_audience')
        if (value = attributes[:'grant_access_token_audience']).is_a?(Array)
          self.grant_access_token_audience = value
        end
      end

      if attributes.key?(:'grant_scope')
        if (value = attributes[:'grant_scope']).is_a?(Array)
          self.grant_scope = value
        end
      end

      if attributes.key?(:'handled_at')
        self.handled_at = attributes[:'handled_at']
      end

      if attributes.key?(:'remember')
        self.remember = attributes[:'remember']
      end

      if attributes.key?(:'remember_for')
        self.remember_for = attributes[:'remember_for']
      end

      if attributes.key?(:'session')
        self.session = attributes[:'session']
      end
    end

    # Show invalid properties with the reasons. Usually used together with valid?
    # @return Array for valid properties with the reasons
    def list_invalid_properties
      invalid_properties = Array.new
      invalid_properties
    end

    # Check to see if the all the properties in the model are valid
    # @return true if the model is valid
    def valid?
      true
    end

    # Checks equality by comparing each attribute.
    # @param [Object] Object to be compared
    def ==(o)
      return true if self.equal?(o)
      self.class == o.class &&
          consent_request == o.consent_request &&
          grant_access_token_audience == o.grant_access_token_audience &&
          grant_scope == o.grant_scope &&
          handled_at == o.handled_at &&
          remember == o.remember &&
          remember_for == o.remember_for &&
          session == o.session
    end

    # @see the `==` method
    # @param [Object] Object to be compared
    def eql?(o)
      self == o
    end

    # Calculates hash code according to all attributes.
    # @return [Integer] Hash code
    def hash
      [consent_request, grant_access_token_audience, grant_scope, handled_at, remember, remember_for, session].hash
    end

    # Builds the object from hash
    # @param [Hash] attributes Model attributes in the form of hash
    # @return [Object] Returns the model itself
    def self.build_from_hash(attributes)
      new.build_from_hash(attributes)
    end

    # Builds the object from hash
    # @param [Hash] attributes Model attributes in the form of hash
    # @return [Object] Returns the model itself
    def build_from_hash(attributes)
      return nil unless attributes.is_a?(Hash)
      self.class.openapi_types.each_pair do |key, type|
        if type =~ /\AArray<(.*)>/i
          # check to ensure the input is an array given that the attribute
          # is documented as an array but the input is not
          if attributes[self.class.attribute_map[key]].is_a?(Array)
            self.send("#{key}=", attributes[self.class.attribute_map[key]].map { |v| _deserialize($1, v) })
          end
        elsif !attributes[self.class.attribute_map[key]].nil?
          self.send("#{key}=", _deserialize(type, attributes[self.class.attribute_map[key]]))
        end # or else data not found in attributes(hash), not an issue as the data can be optional
      end

      self
    end

    # Deserializes the data based on type
    # @param string type Data type
    # @param string value Value to be deserialized
    # @return [Object] Deserialized data
    def _deserialize(type, value)
      case type.to_sym
      when :DateTime
        DateTime.parse(value)
      when :Date
        Date.parse(value)
      when :String
        value.to_s
      when :Integer
        value.to_i
      when :Float
        value.to_f
      when :Boolean
        if value.to_s =~ /\A(true|t|yes|y|1)\z/i
          true
        else
          false
        end
      when :Object
        # generic object (usually a Hash), return directly
        value
      when /\AArray<(?<inner_type>.+)>\z/
        inner_type = Regexp.last_match[:inner_type]
        value.map { |v| _deserialize(inner_type, v) }
      when /\AHash<(?<k_type>.+?), (?<v_type>.+)>\z/
        k_type = Regexp.last_match[:k_type]
        v_type = Regexp.last_match[:v_type]
        {}.tap do |hash|
          value.each do |k, v|
            hash[_deserialize(k_type, k)] = _deserialize(v_type, v)
          end
        end
      else # model
        OryHydraClient.const_get(type).build_from_hash(value)
      end
    end

    # Returns the string representation of the object
    # @return [String] String presentation of the object
    def to_s
      to_hash.to_s
    end

    # to_body is an alias to to_hash (backward compatibility)
    # @return [Hash] Returns the object in the form of hash
    def to_body
      to_hash
    end

    # Returns the object in the form of hash
    # @return [Hash] Returns the object in the form of hash
    def to_hash
      hash = {}
      self.class.attribute_map.each_pair do |attr, param|
        value = self.send(attr)
        if value.nil?
          is_nullable = self.class.openapi_nullable.include?(attr)
          next if !is_nullable || (is_nullable && !instance_variable_defined?(:"@#{attr}"))
        end
        
        hash[param] = _to_hash(value)
      end
      hash
    end

    # Outputs non-array value in the form of hash
    # For object, use to_hash. Otherwise, just return the value
    # @param [Object] value Any valid value
    # @return [Hash] Returns the value in the form of hash
    def _to_hash(value)
      if value.is_a?(Array)
        value.compact.map { |v| _to_hash(v) }
      elsif value.is_a?(Hash)
        {}.tap do |hash|
          value.each { |k, v| hash[k] = _to_hash(v) }
        end
      elsif value.respond_to? :to_hash
        value.to_hash
      else
        value
      end
    end
  end
end

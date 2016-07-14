# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::Web
  module Models
    #
    # Collection of Classic Mobile Services
    #
    class ClassicMobileServiceCollection

      include MsRestAzure

      # @return [Array<ClassicMobileService>] Collection of resources
      attr_accessor :value

      # @return [String] Link to next page of resources
      attr_accessor :next_link


      #
      # Mapper for ClassicMobileServiceCollection class as Ruby Hash.
      # This will be used for serialization/deserialization.
      #
      def self.mapper()
        {
          required: false,
          serialized_name: 'ClassicMobileServiceCollection',
          type: {
            name: 'Composite',
            class_name: 'ClassicMobileServiceCollection',
            model_properties: {
              value: {
                required: false,
                serialized_name: 'value',
                type: {
                  name: 'Sequence',
                  element: {
                      required: false,
                      serialized_name: 'ClassicMobileServiceElementType',
                      type: {
                        name: 'Composite',
                        class_name: 'ClassicMobileService'
                      }
                  }
                }
              },
              next_link: {
                required: false,
                serialized_name: 'nextLink',
                type: {
                  name: 'String'
                }
              }
            }
          }
        }
      end
    end
  end
end
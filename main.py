#
# import csv
# import json
# import requests
#
# # API endpoint
# url = "https://mightyzeus.housing.com/api/gql/stale?apiName=SEARCH_RESULTS&emittedFrom=client_buy_SRP&isBot=false&platform=desktop&source=web&source_name=AudienceWeb"
# payload = {
#     "query": """
#       fragment PR on Property {
#         features {
#           label
#           description
#           id
#         }
#         coverImage {
#           src
#           alt
#           videoUrl
#         }
#         polygonsHash
#         hasAutoVideo
#         imageCount
#         propertyType
#         title
#         subtitle
#         isUc
#         isActiveProperty
#         isMostContacted
#         isRecentlyAdded
#         galleryTitle
#         tracking
#         price
#         displayPrice {
#           value
#           displayValue
#           unit
#           deposit
#           brokerage
#           maintenance
#           displayMaintenance
#           displayDeposit
#           displayBrokerage
#           totalRent
#           brokerageDuration
#           depositDuration
#           displayParkingCharges
#           displayPaintingCharges
#           paintingDuration
#           lockInPeriod
#         }
#         address {
#           address
#           url
#           detailedPropertyAddress {
#             url
#             val
#           }
#           distanceFromEntity
#         }
#         url
#         label
#         badge
#         ownerListingBadge
#         listingId
#         postedDate
#         originalListingId
#         promotions
#         coords
#         propertyInformation
#         tags
#         furnishingType
#         builtUpArea {
#           value
#           unit
#         }
#         sellerCount
#         meta
#         sellers {
#           ...BS
#           phone {
#             partialValue
#           }
#           isCertifiedAgent
#           sellerTag
#           adDeficit
#         }
#         emi
#         brands {
#           name
#         }
#         details {
#           sliceViewUrl
#           images {
#             images {
#               src
#               alt
#               aspectRatio
#               category
#               caption
#             }
#           }
#           config {
#             displayAreaType
#             propertyConfig {
#               key
#               label
#               data {
#                 id
#                 price {
#                   value
#                   displayValue
#                   unit
#                 }
#                 areaConfig {
#                   name
#                   areaInfo {
#                     value
#                     unit
#                     displayArea
#                   }
#                 }
#               }
#             }
#           }
#           propertyConfigs {
#             id
#             icon
#             label
#             description
#             meta
#             showOnMobile
#             mobileLabel
#             formattedDescription
#           }
#         }
#         minDistanceLocality {
#           distance
#           name
#         }
#         isAuctionFlat
#         photoUnderReview
#         propertyTags
#         isMyGateCertified
#         isExclusiveProperty
#       }
#       fragment SR on Property {
#         ...PR
#         certifiedDetails {
#           isVerifiedProperty
#           similarPropertyKeys
#           isCertifiedProperty
#         }
#         description {
#           overviewDescription
#           highlights
#         }
#         videoTour {
#           startDate
#           endDate
#           url
#           meetingNumber
#         }
#         highlights
#         brands {
#           name
#           image
#           theme {
#             color
#           }
#         }
#         boostedAs
#       }
#       fragment BS on User {
#         name
#         id
#         image
#         firmName
#         url
#         type
#         isPrime
#         sellerBadge
#         isPaid
#         designation
#         formattedCustomerServedCount
#       }
#       fragment Ad on SearchResults {
#         nearbyProperties {
#           ...SR
#           nearByPlaces {
#             establishmentType
#             name
#             distance
#           }
#         }
#         promotedProperties {
#           type
#           properties {
#             ...PR
#             videoConnectAvailable
#             micrositeRedirectionURL
#           }
#         }
#         recentlyAddedProperties @include(if: $isRent) {
#           ...SR
#           videoConnectAvailable
#           updatedAt
#           digitour {
#             url
#           }
#           socialUrgency {
#             msg
#           }
#           socialContext {
#             msg
#           }
#         }
#         ownerNearbyProperties {
#           ...SR
#         }
#         collections {
#           title
#           subTitle
#           image
#           propertyCount
#           url
#           key
#         }
#         sellers @include(if: $addSellersData) {
#           name
#           id
#           image
#           firmName
#           url
#           type
#           isPrime
#           sellerBadge
#           isPaid
#           designation
#           stats {
#             label
#             description
#           }
#           meta
#           description
#           sellerDescription
#           cities {
#             id
#             name
#             image
#           }
#           phone {
#             partialValue
#           }
#         }
#       }
#       query(
#         $pageInfo: PageInfoInput
#         $city: CityInput
#         $hash: String!
#         $service: String!
#         $category: String!
#         $meta: JSON
#         $adReq: Boolean!
#         $getStructured: Boolean!
#         $fltcnt: String
#         $isRent: Boolean!
#         $isLandmarkSearchActive: Boolean
#         $addSellersData: Boolean!
#         $interestLedFilter: String
#         $landmarkRelevanceExp: Boolean
#         $isMapSearch: Boolean
#         $lat: Float
#         $lng: Float
#         $outerRadius: Float
#       ) {
#         searchResults(
#           hash: $hash
#           service: $service
#           category: $category
#           city: $city
#           pageInfo: $pageInfo
#           meta: $meta
#           fltcnt: $fltcnt
#           isLandmarkSearchActive: $isLandmarkSearchActive
#           interestLedFilter: $interestLedFilter
#           landmarkRelevanceExp: $landmarkRelevanceExp
#           isMapSearch: $isMapSearch
#           lat: $lat
#           lng: $lng
#           outerRadius: $outerRadius
#         ) {
#           properties {
#             ...SR
#             videoConnectAvailable
#             updatedAt
#             updatedAtStr
#             verifiedAt
#             digitour {
#               url
#             }
#             nearByPlaces {
#               establishmentType
#               name
#               distance
#             }
#             socialUrgency {
#               msg
#             }
#             socialContext {
#               msg
#             }
#             isBrokerageChargeable
#             reviewRating
#             showNewLaunch
#             isTitanium
#             isLocalityChampion
#             distanceFromCoords
#             collageImageUrl
#             details {
#               brochure {
#                 pdf
#                 name
#                 hasBrochure
#               }
#             }
#           }
#           ...Ad @include(if: $adReq)
#           config {
#             filters
#             pageInfo {
#               totalCount
#               size
#               page
#             }
#             entities {
#               id
#               type
#               locationCoordinates
#             }
#           }
#           meta
#           structuredData @include(if: $getStructured)
#           socialProofingIndexes
#           npoPropertiesData {
#             totalCount
#             properties {
#               ...SR
#               videoConnectAvailable
#               updatedAt
#               digitour {
#                 url
#               }
#               nearByPlaces {
#                 establishmentType
#                 name
#                 distance
#               }
#               socialUrgency {
#                 msg
#               }
#               socialContext {
#                 msg
#               }
#               isBrokerageChargeable
#               reviewRating
#               showNewLaunch
#               distanceFromCoords
#               collageImageUrl
#             }
#           }
#         }
#       }
#     """,
#     "variables": "{\"hash\":\"M8vP68l9kmn9yssdkm8k\",\"service\":\"buy\",\"category\":\"residential\",\"city\":{\"name\":\"Hyderabad\",\"id\":\"1cdd81323d5286e9fa47\",\"cityId\":\"df50812912a40e78be9a\",\"url\":\"hyderabad\",\"isTierTwo\":false,\"products\":[\"paying_guest\",\"rent\",\"flatmate\",\"buy\",\"plots\",\"commercial\"]},\"pageInfo\":{\"page\":1,\"size\":30},\"meta\":{\"filterMeta\":{},\"url\":\"/in/buy/property-in-telangana\",\"shouldModifySearchResults\":true,\"pagination_flow\":false,\"enableExperimentalFlag\":false,\"api\":{\"cursor\":\"-1712742407\",\"np_total_count\":8118,\"np_offset\":0,\"resale_offset\":0,\"resale_total_count\":14346}},\"bot\":false,\"getStructured\":false,\"adReq\":false,\"fltcnt\":\"\",\"isRent\":false,\"isLandmarkSearchActive\":true,\"addSellersData\":true,\"interestLedFilter\":\"\",\"isMapSearch\":false,\"lat\":0,\"lng\":0,\"outerRadius\":0}"
# }
#
# # Send the POST request without a payload
# response = requests.post(url,json=payload)
#
# # Check if the response is JSON or HTML
# try:
#     response_json = response.json()
#     print("Response is in JSON format")
# except ValueError:
#     print("Response is not JSON, it might be HTML")
#     print(response.text)
#     exit()
#
# # Extract project details from the JSON response
# projects = response_json['data']['searchResults']['properties']  # Adjust the key to match your JSON structure
#
# # Define the CSV file name
# csv_file = 'projects.csv'
#
# # Open the CSV file in write mode
# with open(csv_file, mode='w', newline='') as file:
#     writer = csv.writer(file)
#
#     # Write the header row
#     writer.writerow(['project_name', 'url'])
#
#     # Write the project data rows
#     for project in projects:
#         project_name = project.get('title', 'N/A')
#         url = project.get('url', 'N/A')
#         writer.writerow([project_name, url])
#         print(f"Project Name: {project_name}")
#         print(f"URL: {url}")
#
# print(f"Data has been written to {csv_file}")

# ---------------------------------------------------------------------------------------------------------------------------
import csv
import json
import time

import requests

# https://mightyzeus.housing.com/api/gql/stale?apiName=SEARCH_RESULTS&emittedFrom=client_buy_SRP&isBot=false&platform=desktop&source=web&source_name=AudienceWeb

# API endpoint
url = "https://mightyzeus.housing.com/api/gql/stale?apiName=SEARCH_RESULTS&emittedFrom=client_buy_SRP&isBot=false&platform=desktop&source=web&source_name=AudienceWeb"
# Initialize the initial cursor value
cursor = "-1688494621"

# Define the CSV file name
csv_file = 'readytomove211.csv'

# Open the CSV file in write mode
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['project_name', 'url'])

    # Loop through pages 1 to 100
    for page in range(1, 211):
        # time.sleep(10)
        # Update the JSON payload with the current page number
        payload = {
            "query": """
  fragment PR on Property {
    features {
      label
      description
      id
    }
    coverImage {
      src
      alt
      videoUrl
    }
    polygonsHash
    hasAutoVideo
    imageCount
    propertyType
    title
    subtitle
    isUc
    isActiveProperty
    isMostContacted
    isRecentlyAdded
    galleryTitle
    tracking
    price
    displayPrice {
      value
      displayValue
      unit
      deposit
      brokerage
      maintenance
      displayMaintenance
      displayDeposit
      displayBrokerage
      totalRent
      brokerageDuration
      depositDuration
      displayParkingCharges
      displayPaintingCharges
      paintingDuration
      lockInPeriod
    }
    address {
      address
      url
      detailedPropertyAddress {
        url
        val
      }
      distanceFromEntity
    }
    url
    label
    badge
    ownerListingBadge
    listingId
    postedDate
    originalListingId
    promotions
    coords
    propertyInformation
    tags
    furnishingType
    builtUpArea {
      value
      unit
    }
    sellerCount
    meta
    sellers {
      ...BS
      phone {
        partialValue
      }
      isCertifiedAgent
      sellerTag
      adDeficit
    }
    emi
    brands {
      name
    }
    details {
      sliceViewUrl
      images {
        images {
          src
          alt
          aspectRatio
          category
          caption
        }
      }
      config {
        displayAreaType
        propertyConfig {
          key
          label
          data {
            id
            price {
              value
              displayValue
              unit
            }
            areaConfig {
              name
              areaInfo {
                value
                unit
                displayArea
              }
            }
          }
        }
      }
      propertyConfigs {
        id
        icon
        label
        description
        meta
        showOnMobile
        mobileLabel
        formattedDescription
      }
    }
    minDistanceLocality {
      distance
      name
    }
    isAuctionFlat
    photoUnderReview
    propertyTags
    isMyGateCertified
    isExclusiveProperty
  }
  fragment SR on Property {
    ...PR
    certifiedDetails {
      isVerifiedProperty
      similarPropertyKeys
      isCertifiedProperty
    }
    description {
      overviewDescription
      highlights
    }
    videoTour {
      startDate
      endDate
      url
      meetingNumber
    }
    highlights
    brands {
      name
      image
      theme {
        color
      }
    }
    boostedAs
  }
  fragment BS on User {
    name
    id
    image
    firmName
    url
    type
    isPrime
    sellerBadge
    isPaid
    designation
    formattedCustomerServedCount
  }
  fragment Ad on SearchResults {
    nearbyProperties {
      ...SR
      nearByPlaces {
        establishmentType
        name
        distance
      }
    }
    promotedProperties {
      type
      properties {
        ...PR
        videoConnectAvailable
        micrositeRedirectionURL
      }
    }
    recentlyAddedProperties @include(if: $isRent) {
      ...SR
      videoConnectAvailable
      updatedAt
      digitour {
        url
      }
      socialUrgency {
        msg
      }
      socialContext {
        msg
      }
    }
    ownerNearbyProperties {
      ...SR
    }
    collections {
      title
      subTitle
      image
      propertyCount
      url
      key
    }
    sellers @include(if: $addSellersData) {
      name
      id
      image
      firmName
      url
      type
      isPrime
      sellerBadge
      isPaid
      designation
      stats {
        label
        description
      }
      meta
      description
      sellerDescription
      cities {
        id
        name
        image
      }
      phone {
        partialValue
      }
    }
  }
  query(
    $pageInfo: PageInfoInput
    $city: CityInput
    $hash: String!
    $service: String!
    $category: String!
    $meta: JSON
    $adReq: Boolean!
    $getStructured: Boolean!
    $fltcnt: String
    $isRent: Boolean!
    $isLandmarkSearchActive: Boolean
    $addSellersData: Boolean!
    $interestLedFilter: String
    $landmarkRelevanceExp: Boolean
    $isMapSearch: Boolean
    $lat: Float
    $lng: Float
    $outerRadius: Float
  ) {
    searchResults(
      hash: $hash
      service: $service
      category: $category
      city: $city
      pageInfo: $pageInfo
      meta: $meta
      fltcnt: $fltcnt
      isLandmarkSearchActive: $isLandmarkSearchActive
      interestLedFilter: $interestLedFilter
      landmarkRelevanceExp: $landmarkRelevanceExp
      isMapSearch: $isMapSearch
      lat: $lat
      lng: $lng
      outerRadius: $outerRadius
    ) {
      properties {
        ...SR
        videoConnectAvailable
        updatedAt
        updatedAtStr
        verifiedAt
        digitour {
          url
        }
        nearByPlaces {
          establishmentType
          name
          distance
        }
        socialUrgency {
          msg
        }
        socialContext {
          msg
        }
        isBrokerageChargeable
        reviewRating
        showNewLaunch
        isTitanium
        isLocalityChampion
        distanceFromCoords
        collageImageUrl
        details {
          brochure {
            pdf
            name
            hasBrochure
          }
        }
      }
      ...Ad @include(if: $adReq)
      config {
        filters
        pageInfo {
          totalCount
          size
          page
        }
        entities {
          id
          type
          locationCoordinates
        }
      }
      meta
      structuredData @include(if: $getStructured)
      socialProofingIndexes
      npoPropertiesData {
        totalCount
        properties {
          ...SR
          videoConnectAvailable
          updatedAt
          digitour {
            url
          }
          nearByPlaces {
            establishmentType
            name
            distance
          }
          socialUrgency {
            msg
          }
          socialContext {
            msg
          }
          isBrokerageChargeable
          reviewRating
          showNewLaunch
          distanceFromCoords
          collageImageUrl
        }
      }
    }
  }
""",
            "variables": json.dumps({
                "hash": "P679xe73u28050522Z7",
    "service": "buy",
    "category": "residential",
    "city": {
        "name": "Hyderabad",
        "id": "1cdd81323d5286e9fa47",
        "cityId": "df50812912a40e78be9a",
        "url": "hyderabad",
        "isTierTwo": False,
        "products": [
            "paying_guest",
            "rent",
            "flatmate",
            "buy",
            "plots",
            "commercial"
        ]
                },
                "pageInfo": {"page": page, "size": 30},
                "meta": {
                    "filterMeta": {},
                    "url": "/in/buy/hyderabad/ready_to_move_projects-hyderabad",
                    "shouldModifySearchResults": True,
                    "pagination_flow": False,
                    "enableExperimentalFlag": False,
                    "api": {
                        "cursor": cursor,  # Assign the current cursor value
                        "np_total_count": 6335,
                        "np_offset": 0,
                        "resale_offset": 0,
                        "resale_total_count": 0
                    }
                },
                "bot": False,
                "getStructured": False,
                "adReq": False,
                "fltcnt": "",
                "isRent": False,
                "isLandmarkSearchActive": True,
                "addSellersData": True,
                "interestLedFilter": "",
                "isMapSearch": False,
                "lat": 0,
                "lng": 0,
                "outerRadius": 0
            })
        }

        # Send the POST request
        response = requests.post(url, json=payload)

        # Check if the response is JSON
        try:
            response_json = response.json()
            print(f"Page {page}: Response is in JSON format")
        except ValueError:
            print(f"Page {page}: Response is not in JSON format")
            continue

        # Extract property data
        properties = response_json.get("data", {}).get("searchResults", {}).get("properties", [])
        # Extract cursor value
        cursor = response_json.get("data", {}).get("searchResults", {}).get("meta", {}).get("api", {}).get("cursor")



        for property in properties:
            project_name = property.get('title')
            project_url = property.get('url')
            if project_name and project_url:
                # Write the data to the CSV file
                writer.writerow([project_name, project_url])
                print(f"Page {page}: Added {project_name} to CSV")
# ----------------------------------------------------------------------------------------------------------------------
# import csv
# import json
# import requests
# from concurrent.futures import ThreadPoolExecutor
# from threading import Lock
#
# # API endpoint
# url = "https://mightyzeus.housing.com/api/gql/stale?apiName=SEARCH_RESULTS&emittedFrom=client_buy_SRP&isBot=false&platform=desktop&source=web&source_name=AudienceWeb"
#
# # Define the CSV file name
# csv_file = 'projects748.csv'
#
# # Create a lock for thread-safe writing to the CSV file
# csv_lock = Lock()
#
# def send_request(page):
#     # Update the JSON payload with the current page number
#     payload = {
#         "query": """
#             fragment PR on Property {
#               features {
#                 label
#                 description
#                 id
#               }
#               coverImage {
#                 src
#                 alt
#                 videoUrl
#               }
#               polygonsHash
#               hasAutoVideo
#               imageCount
#               propertyType
#               title
#               subtitle
#               isUc
#               isActiveProperty
#               isMostContacted
#               isRecentlyAdded
#               galleryTitle
#               tracking
#               price
#               displayPrice {
#                 value
#                 displayValue
#                 unit
#                 deposit
#                 brokerage
#                 maintenance
#                 displayMaintenance
#                 displayDeposit
#                 displayBrokerage
#                 totalRent
#                 brokerageDuration
#                 depositDuration
#                 displayParkingCharges
#                 displayPaintingCharges
#                 paintingDuration
#                 lockInPeriod
#               }
#               address {
#                 address
#                 url
#                 detailedPropertyAddress {
#                   url
#                   val
#                 }
#                 distanceFromEntity
#               }
#               url
#               label
#               badge
#               ownerListingBadge
#               listingId
#               postedDate
#               originalListingId
#               promotions
#               coords
#               propertyInformation
#               tags
#               furnishingType
#               builtUpArea {
#                 value
#                 unit
#               }
#               sellerCount
#               meta
#               sellers {
#                 ...BS
#                 phone {
#                   partialValue
#                 }
#                 isCertifiedAgent
#                 sellerTag
#                 adDeficit
#               }
#               emi
#               brands {
#                 name
#               }
#               details {
#                 sliceViewUrl
#                 images {
#                   images {
#                     src
#                     alt
#                     aspectRatio
#                     category
#                     caption
#                   }
#                 }
#                 config {
#                   displayAreaType
#                   propertyConfig {
#                     key
#                     label
#                     data {
#                       id
#                       price {
#                         value
#                         displayValue
#                         unit
#                       }
#                       areaConfig {
#                         name
#                         areaInfo {
#                           value
#                           unit
#                           displayArea
#                         }
#                       }
#                     }
#                   }
#                 }
#                 propertyConfigs {
#                   id
#                   icon
#                   label
#                   description
#                   meta
#                   showOnMobile
#                   mobileLabel
#                   formattedDescription
#                 }
#               }
#               minDistanceLocality {
#                 distance
#                 name
#               }
#               isAuctionFlat
#               photoUnderReview
#               propertyTags
#               isMyGateCertified
#               isExclusiveProperty
#             }
#             fragment SR on Property {
#               ...PR
#               certifiedDetails {
#                 isVerifiedProperty
#                 similarPropertyKeys
#                 isCertifiedProperty
#               }
#               description {
#                 overviewDescription
#                 highlights
#               }
#               videoTour {
#                 startDate
#                 endDate
#                 url
#                 meetingNumber
#               }
#               highlights
#               brands {
#                 name
#                 image
#                 theme {
#                   color
#                 }
#               }
#               boostedAs
#             }
#             fragment BS on User {
#               name
#               id
#               image
#               firmName
#               url
#               type
#               isPrime
#               sellerBadge
#               isPaid
#               designation
#               formattedCustomerServedCount
#             }
#             fragment Ad on SearchResults {
#               nearbyProperties {
#                 ...SR
#                 nearByPlaces {
#                   establishmentType
#                   name
#                   distance
#                 }
#               }
#               promotedProperties {
#                 type
#                 properties {
#                   ...PR
#                   videoConnectAvailable
#                   micrositeRedirectionURL
#                 }
#               }
#               recentlyAddedProperties @include(if: $isRent) {
#                 ...SR
#                 videoConnectAvailable
#                 updatedAt
#                 digitour {
#                   url
#                 }
#                 socialUrgency {
#                   msg
#                 }
#                 socialContext {
#                   msg
#                 }
#               }
#               ownerNearbyProperties {
#                 ...SR
#               }
#               collections {
#                 title
#                 subTitle
#                 image
#                 propertyCount
#                 url
#                 key
#               }
#               sellers @include(if: $addSellersData) {
#                 name
#                 id
#                 image
#                 firmName
#                 url
#                 type
#                 isPrime
#                 sellerBadge
#                 isPaid
#                 designation
#                 stats {
#                   label
#                   description
#                 }
#                 meta
#                 description
#                 sellerDescription
#                 cities {
#                   id
#                   name
#                   image
#                 }
#                 phone {
#                   partialValue
#                 }
#               }
#             }
#             query(
#               $pageInfo: PageInfoInput
#               $city: CityInput
#               $hash: String!
#               $service: String!
#               $category: String!
#               $meta: JSON
#               $adReq: Boolean!
#               $getStructured: Boolean!
#               $fltcnt: String
#               $isRent: Boolean!
#               $isLandmarkSearchActive: Boolean
#               $addSellersData: Boolean!
#               $interestLedFilter: String
#               $landmarkRelevanceExp: Boolean
#               $isMapSearch: Boolean
#               $lat: Float
#               $lng: Float
#               $outerRadius: Float
#             ) {
#               searchResults(
#                 hash: $hash
#                 service: $service
#                 category: $category
#                 city: $city
#                 pageInfo: $pageInfo
#                 meta: $meta
#                 fltcnt: $fltcnt
#                 isLandmarkSearchActive: $isLandmarkSearchActive
#                 interestLedFilter: $interestLedFilter
#                 landmarkRelevanceExp: $landmarkRelevanceExp
#                 isMapSearch: $isMapSearch
#                 lat: $lat
#                 lng: $lng
#                 outerRadius: $outerRadius
#               ) {
#                 properties {
#                   ...SR
#                   videoConnectAvailable
#                   updatedAt
#                   updatedAtStr
#                   verifiedAt
#                   digitour {
#                     url
#                   }
#                   nearByPlaces {
#                     establishmentType
#                     name
#                     distance
#                   }
#                   socialUrgency {
#                     msg
#                   }
#                   socialContext {
#                     msg
#                   }
#                   isBrokerageChargeable
#                   reviewRating
#                   showNewLaunch
#                   isTitanium
#                   isLocalityChampion
#                   distanceFromCoords
#                   collageImageUrl
#                   details {
#                     brochure {
#                       pdf
#                       name
#                       hasBrochure
#                     }
#                   }
#                 }
#                 ...Ad @include(if: $adReq)
#                 config {
#                   filters
#                   pageInfo {
#                     totalCount
#                     size
#                     page
#                   }
#                   entities {
#                     id
#                     type
#                     locationCoordinates
#                   }
#                 }
#                 meta
#                 structuredData @include(if: $getStructured)
#                 socialProofingIndexes
#                 npoPropertiesData {
#                   totalCount
#                   properties {
#                     ...SR
#                     videoConnectAvailable
#                     updatedAt
#                     digitour {
#                       url
#                     }
#                     nearByPlaces {
#                       establishmentType
#                       name
#                       distance
#                     }
#                     socialUrgency {
#                       msg
#                     }
#                     socialContext {
#                       msg
#                     }
#                     isBrokerageChargeable
#                     reviewRating
#                     showNewLaunch
#                     distanceFromCoords
#                     collageImageUrl
#                   }
#                 }
#               }
#             }
#           """,
#         "variables": json.dumps({
#             "hash": "M8vP68l9kmn9yssdkm8k",
#             "service": "buy",
#             "category": "residential",
#             "city": {
#                 "name": "Hyderabad",
#                 "id": "1cdd81323d5286e9fa47",
#                 "cityId": "df50812912a40e78be9a",
#                 "url": "hyderabad",
#                 "isTierTwo": False,
#                 "products": ["paying_guest", "rent", "flatmate", "buy", "plots", "commercial"]
#             },
#             "pageInfo": {"page": page, "size": 30},
#             "meta": {
#                 "filterMeta": {},
#                 "url": "/in/buy/property-in-telangana",
#                 "shouldModifySearchResults": True,
#                 "pagination_flow": False,
#                 "enableExperimentalFlag": False,
#                 "api": {
#                     "cursor": "-1712742407",
#                     "np_total_count": 8118,
#                     "np_offset": 0,
#                     "resale_offset": 0,
#                     "resale_total_count": 14346
#                 }
#             },
#             "bot": False,
#             "getStructured": False,
#             "adReq": False,
#             "fltcnt": "",
#             "isRent": False,
#             "isLandmarkSearchActive": True,
#             "addSellersData": True,
#             "interestLedFilter": "",
#             "isMapSearch": False,
#             "lat": 0,
#             "lng": 0,
#             "outerRadius": 0
#         })
#     }
#
#     # Send the POST request
#     response = requests.post(url, json=payload)
#
#     # Check if the response is JSON
#     try:
#         response_json = response.json()
#         print(f"Page {page}: Response is in JSON format")
#     except ValueError:
#         print(f"Page {page}: Response is not in JSON format")
#         return
#
#     # Extract property data
#     properties = response_json.get("data", {}).get("searchResults", {}).get("properties", [])
#     for property in properties:
#         project_name = property.get('title')
#         project_url = property.get('url')
#         if project_name and project_url:
#             # Write the data to the CSV file
#             with csv_lock:
#                 with open(csv_file, mode='a', newline='') as file:
#                     writer = csv.writer(file)
#                     writer.writerow([project_name, project_url])
#                     print(f"Page {page}: Added {project_name} to CSV")
#
# # Open the CSV file in write mode and write the header row
# with open(csv_file, mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['project_name', 'url'])
#
# # Create a thread pool with 10 worker threads
# with ThreadPoolExecutor(max_workers=20) as executor:
#     # Submit tasks to the thread pool for pages 3 to 5
#     for page in range(1, 748):
#         executor.submit(send_request, page)

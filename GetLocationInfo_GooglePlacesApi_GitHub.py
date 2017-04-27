from googleplaces import GooglePlaces
import unicodecsv as csv

def main():



	### THIS IS MY PERSONAL KEY. USE YOUR OWN TO NOT REACH LIMIT
	Googlekey = '' #Insert your own google key
	google_places = GooglePlaces(Googlekey)
	
	# PLACES TO SEARCH FOR
	places = ['Khartoum, Sudan', 'Asmara, Eritrea', 'Juba, South Sudan', 'Djibouti, Djibouti', 'Mogadishu, Somalia', 'Bangui, Central African Republic', 'Kampala, Uganda', 'Kinshasa, Democratic Republic of the Congo']
	
	### Key = 1st Element = Type of location I am searching for
	### Value = 2nd Element = keyword I am searching for within the location
	query = {'Diplomatic_Embassy':'embassy', 'Diplomatic_Consulate':'consulate', 'POEE_Airport':'airport', 'POEE_TrainStation':'Main train station', 'POEE_BusStation':'Main bus station', 'Medical':'hospital', 'Hotel_Expensive':'5 star Hotels', 'Hotel_Normal':'Hotels'}



	getPlaces(places, query, google_places)


def getPlaces(places, query, google_places):
	for aSinglePlace in places:

		### Writing all this to a CSV File
		with open ('C:\\Users\\NameOfUser\\Documents\\'+aSinglePlace+'.csv', "ab") as output:
			writer = csv.writer(output, dialect='excel', encoding='utf-8', lineterminator="\n")
			headers = ['Lat', 'Lon', 'location_id', 'name', 'alt_names', 'type', 'type_ranking', 'capabilities', 'address_line1', 'address_line2', 'city', 'postal_code', 'adm1', 'country', 'phone_number', 'email_address', 'web_address', 'notes']
			writer.writerow(headers)
		
		### WHAT TO SEARCH FOR WITHIN THE CITY (You are searching for items that appear to the right of the colon(:)). Left of the colon is the type of location search
			for key,value in query.iteritems():
			
				query_result = google_places.nearby_search(location = aSinglePlace, 
												   		   keyword = value,
												           radius = 50000)
		
				
				for place in query_result.places:
		
					
					### Gets the details of the location
					place.get_details()
		
					### the JSON of the address. This will show why the next step is so long because of the unknown order of the address based on available...
					### ... and missing information
					print place.details['address_components']
		
		
		
					### The type of the address is appended to a list when found. The reason for so many lines is because you never know in what order the address will...
					### ...come in through the JSON 
					try:
						postalCode0 = []
						localityCity0 = []
						adminAreaLevel1State0 = []
						countryName0 = []
						pointOfInterest0 = []
						route0 = []
						sublocalityLevel3 = []
						premise0 = []
						streetNumber = []
						subpremise0 = []
						sublocalityLevel2 = []
						sublocalityLevel1 = []
		
						### 0000000000000000000000000000000000000000000000000000000000000000000000 ###
		
						for types in place.details['address_components'][0]['types']:
							# print types
		
							  # STREET ADDRESS NUMBER
							if types == u'street_number':
								streetNumber.append(place.details['address_components'][0]['long_name'])
								for TheStreetNumber in streetNumber:
									if TheStreetNumber:
										addressStreetNumber = TheStreetNumber.encode('utf-8-sig')
									else: 
										addressStreetNumber = None
		
							  # STREET ADDRESS NAME
							elif types == u'route':
								route0.append(place.details['address_components'][0]['long_name'])
								for route in route0:
									if route:
										addressStreetName = route.encode('utf-8-sig')
									else:
										addressStreetName = None
		
							  # POINT OF INTEREST
							elif types == u'point_of_interest':
								point_of_interest0.append(place.details['address_components'][0]['long_name'])
								for ThePointOfInterest in point_of_interest0:
									if ThePointOfInterest:
										pointOfInterest = ThePointOfInterest.encode('utf-8-sig')
									else:
										pointOfInterest = None
		
							  # PREMISE
							elif types == u'premise':
								premise0.append(place.details['address_components'][0]['long_name'])
								for ThePremise in premise0:
									if ThePremise:
										premise = ThePremise.encode('utf-8-sig')
									else:
										premise = None
		
							  # SUBPREMISE
							elif types == u'subpremise':
								subpremise0.append(place.details['address_components'][0]['long_name'])
								for TheSubpremise in subpremise0:
									if TheSubpremise:
										subpremise = TheSubpremise.encode('utf-8-sig')
									else:
										subpremise = None
		
		
							  # CITY NAME
							elif types == u'locality':
								localityCity0.append(place.details['address_components'][0]['long_name'])
								for locality in localityCity0:
									if locality:
										cityName = locality.encode('utf-8-sig')
									else:
										cityName = None
		
							  # STATE NAME
							elif types == u'administrative_area_level_1':
								adminAreaLevel1State0.append(place.details['address_components'][0]['long_name'])
								for stateName in adminAreaLevel1State0:
									if stateName:
										state = stateName.encode('utf-8-sig')
									else:
										state = None
		
							  # POSTAL CODE
							elif types == u'postal_code':
								postalCode0.append(place.details['address_components'][0]['long_name'])
								for ThePostalCode in postalCode0:
									if ThePostalCode:
										postal_code1 = ThePostalCode.encode('utf-8-sig')
									else:
										postal_code1 = None
		
							  # COUNTRY NAME	
							elif types == u'country':
								countryName0.append(place.details['address_components'][0]['long_name'])
								for countryName in countryName0:
									if countryName:
										countryNameIdentified = countryName.encode('utf-8-sig')
									else:
										countryNameIdentified = None
		
							# Sublocality Level 1
							elif types == u'sublocality_level_1':
								sublocalityLevel1.append(place.details['address_components'][0]['long_name'])
								for sublocalityL1 in sublocalityLevel1:
									if sublocalityL1:
										sublocality_area_level_1 = sublocalityL1.encode('utf-8-sig')
									else:
										sublocality_area_level_1 = None
							
							# Sublocality Level2
							elif types =='sublocality_level_2':
								sublocalityLevel2.append(place.details['address_components'][0]['long_name'])
								for sublocalityL2 in sublocalityLevel2:
									if sublocalityL2:
										sublocality_area_level_2 = sublocalityL2.encode('utf-8-sig')
									else:
										sublocality_area_level_2 = None
		
							# Sublocality Level3
							elif types == u'sublocality_level_3':
								sublocalityLevel3.append(place.details['address_components'][0]['long_name'])
								for sublocalityL3 in sublocalityLevel3:
									if sublocalityL3:
										sublocality_area_level_3 = sublocalityL3.encode('utf-8-sig')
									else:
										sublocality_area_level_3 = None
		
							else:
								pass
		
						### 1111111111111111111111111111111111111111111111111111111111111111111 ###
		
						for types in place.details['address_components'][1]['types']:
							# print types
		
							  # STREET ADDRESS NUMBER
							if types == u'street_number':
								streetNumber.append(place.details['address_components'][1]['long_name'])
								for TheStreetNumber in streetNumber:
									if TheStreetNumber:
										addressStreetNumber = TheStreetNumber.encode('utf-8-sig')
									else: 
										addressStreetNumber = None
		
							  # STREET ADDRESS NAME
							elif types == u'route':
								route0.append(place.details['address_components'][1]['long_name'])
								for route in route0:
									if route:
										addressStreetName = route.encode('utf-8-sig')
									else:
										addressStreetName = None
		
							  # POINT OF INTEREST
							elif types == u'point_of_interest':
								point_of_interest0.append(place.details['address_components'][1]['long_name'])
								for ThePointOfInterest in point_of_interest0:
									if ThePointOfInterest:
										pointOfInterest = ThePointOfInterest.encode('utf-8-sig')
									else:
										pointOfInterest = None
		
							  # PREMISE
							elif types == u'premise':
								premise0.append(place.details['address_components'][1]['long_name'])
								for ThePremise in premise0:
									if ThePremise:
										premise = ThePremise.encode('utf-8-sig')
									else:
										premise = None
		
							  # SUBPREMISE
							elif types == u'subpremise':
								subpremise0.append(place.details['address_components'][1]['long_name'])
								for TheSubpremise in subpremise0:
									if TheSubpremise:
										subpremise = TheSubpremise.encode('utf-8-sig')
									else:
										subpremise = None
		
		
							  # CITY NAME
							elif types == u'locality':
								localityCity0.append(place.details['address_components'][1]['long_name'])
								for locality in localityCity0:
									if locality:
										cityName = locality.encode('utf-8-sig')
									else:
										cityName = None
		
							  # STATE NAME
							elif types == u'administrative_area_level_1':
								adminAreaLevel1State0.append(place.details['address_components'][1]['long_name'])
								for stateName in adminAreaLevel1State0:
									if stateName:
										state = stateName.encode('utf-8-sig')
									else:
										state = None
		
							  # POSTAL CODE
							elif types == u'postal_code':
								postalCode0.append(place.details['address_components'][1]['long_name'])
								for ThePostalCode in postalCode0:
									if ThePostalCode:
										postal_code1 = ThePostalCode.encode('utf-8-sig')
									else:
										postal_code1 = None
		
							  # COUNTRY NAME	
							elif types == u'country':
								countryName0.append(place.details['address_components'][1]['long_name'])
								for countryName in countryName0:
									if countryName:
										countryNameIdentified = countryName.encode('utf-8-sig')
									else:
										countryNameIdentified = None
							
							# Sublocatlity Level 1
							elif types == u'sublocality_level_1':
								sublocalityLevel1.append(place.details['address_components'][1]['long_name'])
								for sublocalityL1 in sublocalityLevel1:
									if sublocalityL1:
										sublocality_area_level_1 = sublocalityL1.encode('utf-8-sig')
									else:
										sublocality_area_level_1 = None

							# Sublocatlity Level 2
							elif types =='sublocality_level_2':
								sublocalityLevel2.append(place.details['address_components'][1]['long_name'])
								for sublocalityL2 in sublocalityLevel2:
									if sublocalityL2:
										sublocality_area_level_2 = sublocalityL2.encode('utf-8-sig')
									else:
										sublocality_area_level_2 = None

							# Sublocatlity Level 3
							elif types == u'sublocality_level_3':
								sublocalityLevel3.append(place.details['address_components'][1]['long_name'])
								for sublocalityL3 in sublocalityLevel3:
									if sublocalityL3:
										sublocality_area_level_3 = sublocalityL3.encode('utf-8-sig')
									else:
										sublocality_area_level_3 = None
		
							else:
								pass
		
						### 222222222222222222222222222222222222222222222222222222222222222222 ###
		
						for types in place.details['address_components'][2]['types']:
							# print types
		
							  # STREET ADDRESS NUMBER
							if types == u'street_number':
								streetNumber.append(place.details['address_components'][2]['long_name'])
								for TheStreetNumber in streetNumber:
									if TheStreetNumber:
										addressStreetNumber = TheStreetNumber.encode('utf-8-sig')
									else: 
										addressStreetNumber = None
		
							  # STREET ADDRESS NAME
							elif types == u'route':
								route0.append(place.details['address_components'][2]['long_name'])
								for route in route0:
									if route:
										addressStreetName = route.encode('utf-8-sig')
									else:
										addressStreetName = None
		
							  # POINT OF INTEREST
							elif types == u'point_of_interest':
								point_of_interest0.append(place.details['address_components'][2]['long_name'])
								for ThePointOfInterest in point_of_interest0:
									if ThePointOfInterest:
										pointOfInterest = ThePointOfInterest.encode('utf-8-sig')
									else:
										pointOfInterest = None
		
							  # PREMISE
							elif types == u'premise':
								premise0.append(place.details['address_components'][2]['long_name'])
								for ThePremise in premise0:
									if ThePremise:
										premise = ThePremise.encode('utf-8-sig')
									else:
										premise = None
		
							  # SUBPREMISE
							elif types == u'subpremise':
								subpremise0.append(place.details['address_components'][2]['long_name'])
								for TheSubpremise in subpremise0:
									if TheSubpremise:
										subpremise = TheSubpremise.encode('utf-8-sig')
									else:
										subpremise = None
		
		
							  # CITY NAME
							elif types == u'locality':
								localityCity0.append(place.details['address_components'][2]['long_name'])
								for locality in localityCity0:
									if locality:
										cityName = locality.encode('utf-8-sig')
									else:
										cityName = None
		
							  # STATE NAME
							elif types == u'administrative_area_level_1':
								adminAreaLevel1State0.append(place.details['address_components'][2]['long_name'])
								for stateName in adminAreaLevel1State0:
									if stateName:
										state = stateName.encode('utf-8-sig')
									else:
										state = None
		
							  # POSTAL CODE
							elif types == u'postal_code':
								postalCode0.append(place.details['address_components'][2]['long_name'])
								for ThePostalCode in postalCode0:
									if ThePostalCode:
										postal_code1 = ThePostalCode.encode('utf-8-sig')
									else:
										postal_code1 = None
		
							  # COUNTRY NAME	
							elif types == u'country':
								countryName0.append(place.details['address_components'][2]['long_name'])
								for countryName in countryName0:
									if countryName:
										countryNameIdentified = countryName.encode('utf-8-sig')
									else:
										countryNameIdentified = None
		
							# Sublocatlity Level 1
							elif types == u'sublocality_level_1':
								sublocalityLevel1.append(place.details['address_components'][2]['long_name'])
								for sublocalityL1 in sublocalityLevel1:
									if sublocalityL1:
										sublocality_area_level_1 = sublocalityL1.encode('utf-8-sig')
									else:
										sublocality_area_level_1 = None
		 					
		 					# Sublocatlity Level 2
							elif types =='sublocality_level_2':
								sublocalityLevel2.append(place.details['address_components'][2]['long_name'])
								for sublocalityL2 in sublocalityLevel2:
									if sublocalityL2:
										sublocality_area_level_2 = sublocalityL2.encode('utf-8-sig')
									else:
										sublocality_area_level_2 = None
		
							# Sublocatlity Level 3
							elif types == u'sublocality_level_3':
								sublocalityLevel3.append(place.details['address_components'][2]['long_name'])
								for sublocalityL3 in sublocalityLevel3:
									if sublocalityL3:
										sublocality_area_level_3 = sublocalityL3.encode('utf-8-sig')
									else:
										sublocality_area_level_3 = None
		
							else:
								pass
		
		
						### 333333333333333333333333333333333333333333333333333333333333333333 ###
		
		
						for types in place.details['address_components'][3]['types']:
							# print types
		
							  # STREET ADDRESS NUMBER
							if types == u'street_number':
								streetNumber.append(place.details['address_components'][3]['long_name'])
								for TheStreetNumber in streetNumber:
									if TheStreetNumber:
										addressStreetNumber = TheStreetNumber.encode('utf-8-sig')
									else: 
										addressStreetNumber = None
		
							  # STREET ADDRESS NAME
							elif types == u'route':
								route0.append(place.details['address_components'][3]['long_name'])
								for route in route0:
									if route:
										addressStreetName = route.encode('utf-8-sig')
									else:
										addressStreetName = None
		
							  # POINT OF INTEREST
							elif types == u'point_of_interest':
								point_of_interest0.append(place.details['address_components'][3]['long_name'])
								for ThePointOfInterest in point_of_interest0:
									if ThePointOfInterest:
										pointOfInterest = ThePointOfInterest.encode('utf-8-sig')
									else:
										pointOfInterest = None
		
							  # PREMISE
							elif types == u'premise':
								premise0.append(place.details['address_components'][3]['long_name'])
								for ThePremise in premise0:
									if ThePremise:
										premise = ThePremise.encode('utf-8-sig')
									else:
										premise = None
		
							  # SUBPREMISE
							elif types == u'subpremise':
								subpremise0.append(place.details['address_components'][3]['long_name'])
								for TheSubpremise in subpremise0:
									if TheSubpremise:
										subpremise = TheSubpremise.encode('utf-8-sig')
									else:
										subpremise = None
		
		
							  # CITY NAME
							elif types == u'locality':
								localityCity0.append(place.details['address_components'][3]['long_name'])
								for locality in localityCity0:
									if locality:
										cityName = locality.encode('utf-8-sig')
									else:
										cityName = None
		
							  # STATE NAME
							elif types == u'administrative_area_level_1':
								adminAreaLevel1State0.append(place.details['address_components'][3]['long_name'])
								for stateName in adminAreaLevel1State0:
									if stateName:
										state = stateName.encode('utf-8-sig')
									else:
										state = None
		
							  # POSTAL CODE
							elif types == u'postal_code':
								postalCode0.append(place.details['address_components'][3]['long_name'])
								for ThePostalCode in postalCode0:
									if ThePostalCode:
										postal_code1 = ThePostalCode.encode('utf-8-sig')
									else:
										postal_code1 = None
		
							  # COUNTRY NAME	
							elif types == u'country':
								countryName0.append(place.details['address_components'][3]['long_name'])
								for countryName in countryName0:
									if countryName:
										countryNameIdentified = countryName.encode('utf-8-sig')
									else:
										countryNameIdentified = None
		
							# Sublocatlity Level 1
							elif types == u'sublocality_level_1':
								sublocalityLevel1.append(place.details['address_components'][3]['long_name'])
								for sublocalityL1 in sublocalityLevel1:
									if sublocalityL1:
										sublocality_area_level_1 = sublocalityL1.encode('utf-8-sig')
									else:
										sublocality_area_level_1 = None
							
							# Sublocatlity Level 2
							elif types =='sublocality_level_2':
								sublocalityLevel2.append(place.details['address_components'][3]['long_name'])
								for sublocalityL2 in sublocalityLevel2:
									if sublocalityL2:
										sublocality_area_level_2 = sublocalityL2.encode('utf-8-sig')
									else:
										sublocality_area_level_2 = None
		
							# Sublocatlity Level 3
							elif types == u'sublocality_level_3':
								sublocalityLevel3.append(place.details['address_components'][3]['long_name'])
								for sublocalityL3 in sublocalityLevel3:
									if sublocalityL3:
										sublocality_area_level_3 = sublocalityL3.encode('utf-8-sig')
									else:
										sublocality_area_level_3 = None
		
							else:
								pass
						### 44444444444444444444444444444444444444444444444444444444444444444 ###
		
						for types in place.details['address_components'][4]['types']:
							# print types
		
							  # STREET ADDRESS NUMBER
							if types == u'street_number':
								streetNumber.append(place.details['address_components'][4]['long_name'])
								for TheStreetNumber in streetNumber:
									if TheStreetNumber:
										addressStreetNumber = TheStreetNumber.encode('utf-8-sig')
									else: 
										addressStreetNumber = None
		
							  # STREET ADDRESS NAME
							elif types == u'route':
								route0.append(place.details['address_components'][4]['long_name'])
								for route in route0:
									if route:
										addressStreetName = route.encode('utf-8-sig')
									else:
										addressStreetName = None
		
							  # POINT OF INTEREST
							elif types == u'point_of_interest':
								point_of_interest0.append(place.details['address_components'][4]['long_name'])
								for ThePointOfInterest in point_of_interest0:
									if ThePointOfInterest:
										pointOfInterest = ThePointOfInterest.encode('utf-8-sig')
									else:
										pointOfInterest = None
		
							  # PREMISE
							elif types == u'premise':
								premise0.append(place.details['address_components'][4]['long_name'])
								for ThePremise in premise0:
									if ThePremise:
										premise = ThePremise.encode('utf-8-sig')
									else:
										premise = None
		
							  # SUBPREMISE
							elif types == u'subpremise':
								subpremise0.append(place.details['address_components'][4]['long_name'])
								for TheSubpremise in subpremise0:
									if TheSubpremise:
										subpremise = TheSubpremise.encode('utf-8-sig')
									else:
										subpremise = None
		
		
							  # CITY NAME
							elif types == u'locality':
								localityCity0.append(place.details['address_components'][4]['long_name'])
								for locality in localityCity0:
									if locality:
										cityName = locality.encode('utf-8-sig')
									else:
										cityName = None
		
							  # STATE NAME
							elif types == u'administrative_area_level_1':
								adminAreaLevel1State0.append(place.details['address_components'][4]['long_name'])
								for stateName in adminAreaLevel1State0:
									if stateName:
										state = stateName.encode('utf-8-sig')
									else:
										state = None
		
							  # POSTAL CODE
							elif types == u'postal_code':
								postalCode0.append(place.details['address_components'][4]['long_name'])
								for ThePostalCode in postalCode0:
									if ThePostalCode:
										postal_code1 = ThePostalCode.encode('utf-8-sig')
									else:
										postal_code1 = None
		
							  # COUNTRY NAME	
							elif types == u'country':
								countryName0.append(place.details['address_components'][4]['long_name'])
								for countryName in countryName0:
									if countryName:
										countryNameIdentified = countryName.encode('utf-8-sig')
									else:
										countryNameIdentified = None
							
							# Sublocatlity Level 1
							elif types == u'sublocality_level_1':
								sublocalityLevel1.append(place.details['address_components'][4]['long_name'])
								for sublocalityL1 in sublocalityLevel1:
									if sublocalityL1:
										sublocality_area_level_1 = sublocalityL1.encode('utf-8-sig')
									else:
										sublocality_area_level_1 = None
							
							# Sublocatlity Level 2
							elif types =='sublocality_level_2':
								sublocalityLevel2.append(place.details['address_components'][4]['long_name'])
								for sublocalityL2 in sublocalityLevel2:
									if sublocalityL2:
										sublocality_area_level_2 = sublocalityL2.encode('utf-8-sig')
									else:
										sublocality_area_level_2 = None
							
							# Sublocatlity Level 3
							elif types == u'sublocality_level_3':
								sublocalityLevel3.append(place.details['address_components'][4]['long_name'])
								for sublocalityL3 in sublocalityLevel3:
									if sublocalityL3:
										sublocality_area_level_3 = sublocalityL3.encode('utf-8-sig')
									else:
										sublocality_area_level_3 = None
		
							else:
								pass
		
						### 555555555555555555555555555555555555555555555555555555555555555 ###
		
						for types in place.details['address_components'][5]['types']:
							# print types
		
							  # STREET ADDRESS NUMBER
							if types == u'street_number':
								streetNumber.append(place.details['address_components'][5]['long_name'])
								for TheStreetNumber in streetNumber:
									if TheStreetNumber:
										addressStreetNumber = TheStreetNumber.encode('utf-8-sig')
									else: 
										addressStreetNumber = None
		
							  # STREET ADDRESS NAME
							elif types == u'route':
								route0.append(place.details['address_components'][5]['long_name'])
								for route in route0:
									if route:
										addressStreetName = route.encode('utf-8-sig')
									else:
										addressStreetName = None
		
							  # POINT OF INTEREST
							elif types == u'point_of_interest':
								point_of_interest0.append(place.details['address_components'][5]['long_name'])
								for ThePointOfInterest in point_of_interest0:
									if ThePointOfInterest:
										pointOfInterest = ThePointOfInterest.encode('utf-8-sig')
									else:
										pointOfInterest = None
		
							  # PREMISE
							elif types == u'premise':
								premise0.append(place.details['address_components'][5]['long_name'])
								for ThePremise in premise0:
									if ThePremise:
										premise = ThePremise.encode('utf-8-sig')
									else:
										premise = None
		
							  # SUBPREMISE
							elif types == u'subpremise':
								subpremise0.append(place.details['address_components'][5]['long_name'])
								for TheSubpremise in subpremise0:
									if TheSubpremise:
										subpremise = TheSubpremise.encode('utf-8-sig')
									else:
										subpremise = None
		
		
							  # CITY NAME
							elif types == u'locality':
								localityCity0.append(place.details['address_components'][5]['long_name'])
								for locality in localityCity0:
									if locality:
										cityName = locality.encode('utf-8-sig')
									else:
										cityName = None
		
							  # STATE NAME
							elif types == u'administrative_area_level_1':
								adminAreaLevel1State0.append(place.details['address_components'][5]['long_name'])
								for stateName in adminAreaLevel1State0:
									if stateName:
										state = stateName.encode('utf-8-sig')
									else:
										state = None
		
							  # POSTAL CODE
							elif types == u'postal_code':
								postalCode0.append(place.details['address_components'][5]['long_name'])
								for ThePostalCode in postalCode0:
									if ThePostalCode:
										postal_code1 = ThePostalCode.encode('utf-8-sig')
									else:
										postal_code1 = None
		
							  # COUNTRY NAME	
							elif types == u'country':
								countryName0.append(place.details['address_components'][5]['long_name'])
								for countryName in countryName0:
									if countryName:
										countryNameIdentified = countryName.encode('utf-8-sig')
									else:
										countryNameIdentified = None
							
							# Sublocatlity Level 1
							elif types == u'sublocality_level_1':
								sublocalityLevel1.append(place.details['address_components'][5]['long_name'])
								for sublocalityL1 in sublocalityLevel1:
									if sublocalityL1:
										sublocality_area_level_1 = sublocalityL1.encode('utf-8-sig')
									else:
										sublocality_area_level_1 = None
							
							# # Sublocatlity Level 2
							elif types =='sublocality_level_2':
								sublocalityLevel2.append(place.details['address_components'][5]['long_name'])
								for sublocalityL2 in sublocalityLevel2:
									if sublocalityL2:
										sublocality_area_level_2 = sublocalityL2.encode('utf-8-sig')
									else:
										sublocality_area_level_2 = None
							
							# Sublocatlity Level 3
							elif types == u'sublocality_level_3':
								sublocalityLevel3.append(place.details['address_components'][5]['long_name'])
								for sublocalityL3 in sublocalityLevel3:
									if sublocalityL3:
										sublocality_area_level_3 = sublocalityL3.encode('utf-8-sig')
									else:
										sublocality_area_level_3 = None
		
							else:
								pass
		
						### 666666666666666666666666666666666666666666666666666666666666 ###
		
						for types in place.details['address_components'][6]['types']:
							# print types
		
							  # STREET ADDRESS NUMBER
							if types == u'street_number':
								streetNumber.append(place.details['address_components'][6]['long_name'])
								for TheStreetNumber in streetNumber:
									if TheStreetNumber:
										addressStreetNumber = TheStreetNumber.encode('utf-8-sig')
									else: 
										addressStreetNumber = None
		
							  # STREET ADDRESS NAME
							elif types == u'route':
								route0.append(place.details['address_components'][6]['long_name'])
								for route in route0:
									if route:
										addressStreetName = route.encode('utf-8-sig')
									else:
										addressStreetName = None
		
							  # POINT OF INTEREST
							elif types == u'point_of_interest':
								point_of_interest0.append(place.details['address_components'][6]['long_name'])
								for ThePointOfInterest in point_of_interest0:
									if ThePointOfInterest:
										pointOfInterest = ThePointOfInterest.encode('utf-8-sig')
									else:
										pointOfInterest = None
		
							  # PREMISE
							elif types == u'premise':
								premise0.append(place.details['address_components'][6]['long_name'])
								for ThePremise in premise0:
									if ThePremise:
										premise = ThePremise.encode('utf-8-sig')
									else:
										premise = None
		
							  # SUBPREMISE
							elif types == u'subpremise':
								subpremise0.append(place.details['address_components'][6]['long_name'])
								for TheSubpremise in subpremise0:
									if TheSubpremise:
										subpremise = TheSubpremise.encode('utf-8-sig')
									else:
										subpremise = None
		
		
							  # CITY NAME
							elif types == u'locality':
								localityCity0.append(place.details['address_components'][6]['long_name'])
								for locality in localityCity0:
									if locality:
										cityName = locality.encode('utf-8-sig')
									else:
										cityName = None
		
							  # STATE NAME
							elif types == u'administrative_area_level_1':
								adminAreaLevel1State0.append(place.details['address_components'][6]['long_name'])
								for stateName in adminAreaLevel1State0:
									if stateName:
										state = stateName.encode('utf-8-sig')
									else:
										state = None
		
							  # POSTAL CODE
							elif types == u'postal_code':
								postalCode0.append(place.details['address_components'][6]['long_name'])
								for ThePostalCode in postalCode0:
									if ThePostalCode:
										postal_code1 = ThePostalCode.encode('utf-8-sig')
									else:
										postal_code1 = None
		
							  # COUNTRY NAME	
							elif types == u'country':
								countryName0.append(place.details['address_components'][6]['long_name'])
								for countryName in countryName0:
									if countryName:
										countryNameIdentified = countryName.encode('utf-8-sig')
									else:
										countryNameIdentified = None
		
							# Sublocatlity Level 1
							elif types == u'sublocality_level_1':
								sublocalityLevel1.append(place.details['address_components'][6]['long_name'])
								for sublocalityL1 in sublocalityLevel1:
									if sublocalityL1:
										sublocality_area_level_1 = sublocalityL1.encode('utf-8-sig')
									else:
										sublocality_area_level_1 = None
		
							# Sublocatlity Level 2
							elif types =='sublocality_level_2':
								sublocalityLevel2.append(place.details['address_components'][6]['long_name'])
								for sublocalityL2 in sublocalityLevel2:
									if sublocalityL2:
										sublocality_area_level_2 = sublocalityL2.encode('utf-8-sig')
									else:
										sublocality_area_level_2 = None
		
							# Sublocatlity Level 3
							elif types == u'sublocality_level_3':
								sublocalityLevel3.append(place.details['address_components'][6]['long_name'])
								for sublocalityL3 in sublocalityLevel3:
									if sublocalityL3:
										sublocality_area_level_3 = sublocalityL3.encode('utf-8-sig')
									else:
										sublocality_area_level_3 = None
		
							else:
								pass
		
						### 777777777777777777777777777777777777777777777777777777777777777 ###
		
						for types in place.details['address_components'][8]['types']:
							# print types
		
							  # STREET ADDRESS NUMBER
							if types == u'street_number':
								streetNumber.append(place.details['address_components'][8]['long_name'])
								for TheStreetNumber in streetNumber:
									if TheStreetNumber:
										addressStreetNumber = TheStreetNumber.encode('utf-8-sig')
									else: 
										addressStreetNumber = None
		
							  # STREET ADDRESS NAME
							elif types == u'route':
								route0.append(place.details['address_components'][8]['long_name'])
								for route in route0:
									if route:
										addressStreetName = route.encode('utf-8-sig')
									else:
										addressStreetName = None
		
							  # POINT OF INTEREST
							elif types == u'point_of_interest':
								point_of_interest0.append(place.details['address_components'][8]['long_name'])
								for ThePointOfInterest in point_of_interest0:
									if ThePointOfInterest:
										pointOfInterest = ThePointOfInterest.encode('utf-8-sig')
									else:
										pointOfInterest = None
		
							  # PREMISE
							elif types == u'premise':
								premise0.append(place.details['address_components'][8]['long_name'])
								for ThePremise in premise0:
									if ThePremise:
										premise = ThePremise.encode('utf-8-sig')
									else:
										premise = None
		
							  # SUBPREMISE
							elif types == u'subpremise':
								subpremise0.append(place.details['address_components'][8]['long_name'])
								for TheSubpremise in subpremise0:
									if TheSubpremise:
										subpremise = TheSubpremise.encode('utf-8-sig')
									else:
										subpremise = None
		
		
							  # CITY NAME
							elif types == u'locality':
								localityCity0.append(place.details['address_components'][8]['long_name'])
								for locality in localityCity0:
									if locality:
										cityName = locality.encode('utf-8-sig')
									else:
										cityName = None
		
							  # STATE NAME
							elif types == u'administrative_area_level_1':
								adminAreaLevel1State0.append(place.details['address_components'][8]['long_name'])
								for stateName in adminAreaLevel1State0:
									if stateName:
										state = stateName.encode('utf-8-sig')
									else:
										state = None
		
							  # POSTAL CODE
							elif types == u'postal_code':
								postalCode0.append(place.details['address_components'][8]['long_name'])
								for ThePostalCode in postalCode0:
									if ThePostalCode:
										postal_code1 = ThePostalCode.encode('utf-8-sig')
									else:
										postal_code1 = None
		
							  # COUNTRY NAME	
							elif types == u'country':
								countryName0.append(place.details['address_components'][8]['long_name'])
								for countryName in countryName0:
									if countryName:
										countryNameIdentified = countryName.encode('utf-8-sig')
									else:
										countryNameIdentified = None
		
							# Sublocatlity Level 1
							elif types == u'sublocality_level_1':
								sublocalityLevel1.append(place.details['address_components'][8]['long_name'])
								for sublocalityL1 in sublocalityLevel1:
									if sublocalityL1:
										sublocality_area_level_1 = sublocalityL1.encode('utf-8-sig')
									else:
										sublocality_area_level_1 = None
		
							# Sublocatlity Level 2
							elif types =='sublocality_level_2':
								sublocalityLevel2.append(place.details['address_components'][8]['long_name'])
								for sublocalityL2 in sublocalityLevel2:
									if sublocalityL2:
										sublocality_area_level_2 = sublocalityL2.encode('utf-8-sig')
									else:
										sublocality_area_level_2 = None
		
							# Sublocatlity Level 3
							elif types == u'sublocality_level_3':
								sublocalityLevel3.append(place.details['address_components'][8]['long_name'])
								for sublocalityL3 in sublocalityLevel3:
									if sublocalityL3:
										sublocality_area_level_3 = sublocalityL3.encode('utf-8-sig')
									else:
										sublocality_area_level_3 = None
		
							else:
								pass
		
						### 88888888888888888888888888888888888888888888888 ###
		
						for types in place.details['address_components'][8]['types']:
							# print types
		
							  # STREET ADDRESS NUMBER
							if types == u'street_number':
								streetNumber.append(place.details['address_components'][8]['long_name'])
								for TheStreetNumber in streetNumber:
									if TheStreetNumber:
										addressStreetNumber = TheStreetNumber.encode('utf-8-sig')
									else: 
										addressStreetNumber = None
		
							  # STREET ADDRESS NAME
							elif types == u'route':
								route0.append(place.details['address_components'][8]['long_name'])
								for route in route0:
									if route:
										addressStreetName = route.encode('utf-8-sig')
									else:
										addressStreetName = None
		
							  # POINT OF INTEREST
							elif types == u'point_of_interest':
								point_of_interest0.append(place.details['address_components'][8]['long_name'])
								for ThePointOfInterest in point_of_interest0:
									if ThePointOfInterest:
										pointOfInterest = ThePointOfInterest.encode('utf-8-sig')
									else:
										pointOfInterest = None
		
							  # PREMISE
							elif types == u'premise':
								premise0.append(place.details['address_components'][8]['long_name'])
								for ThePremise in premise0:
									if ThePremise:
										premise = ThePremise.encode('utf-8-sig')
									else:
										premise = None
		
							  # SUBPREMISE
							elif types == u'subpremise':
								subpremise0.append(place.details['address_components'][8]['long_name'])
								for TheSubpremise in subpremise0:
									if TheSubpremise:
										subpremise = TheSubpremise.encode('utf-8-sig')
									else:
										subpremise = None
		
		
							  # CITY NAME
							elif types == u'locality':
								localityCity0.append(place.details['address_components'][8]['long_name'])
								for locality in localityCity0:
									if locality:
										cityName = locality.encode('utf-8-sig')
									else:
										cityName = None
		
							  # STATE NAME
							elif types == u'administrative_area_level_1':
								adminAreaLevel1State0.append(place.details['address_components'][8]['long_name'])
								for stateName in adminAreaLevel1State0:
									if stateName:
										state = stateName.encode('utf-8-sig')
									else:
										state = None
		
							  # POSTAL CODE
							elif types == u'postal_code':
								postalCode0.append(place.details['address_components'][8]['long_name'])
								for ThePostalCode in postalCode0:
									if ThePostalCode:
										postal_code1 = ThePostalCode.encode('utf-8-sig')
									else:
										postal_code1 = None
		
							  # COUNTRY NAME	
							elif types == u'country':
								countryName0.append(place.details['address_components'][8]['long_name'])
								for countryName in countryName0:
									if countryName:
										countryNameIdentified = countryName.encode('utf-8-sig')
									else:
										countryNameIdentified = None
							
							# Sublocatlity Level 1
							elif types == u'sublocality_level_1':
								sublocalityLevel1.append(place.details['address_components'][8]['long_name'])
								for sublocalityL1 in sublocalityLevel1:
									if sublocalityL1:
										sublocality_area_level_1 = sublocalityL1.encode('utf-8-sig')
									else:
										sublocality_area_level_1 = None
		
							# Sublocatlity Level 2
							elif types =='sublocality_level_2':
								sublocalityLevel2.append(place.details['address_components'][8]['long_name'])
								for sublocalityL2 in sublocalityLevel2:
									if sublocalityL2:
										sublocality_area_level_2 = sublocalityL2.encode('utf-8-sig')
									else:
										sublocality_area_level_2 = None
							
							# Sublocatlity Level 3
							elif types == u'sublocality_level_3':
								sublocalityLevel3.append(place.details['address_components'][8]['long_name'])
								for sublocalityL3 in sublocalityLevel3:
									if sublocalityL3:
										sublocality_area_level_3 = sublocalityL3.encode('utf-8-sig')
									else:
										sublocality_area_level_3 = None
		
							else:
								pass
		
						### 99999999999999999999999999999999999999999999999999999 ###
		
						for types in place.details['address_components'][9]['types']:
							# print types
		
							  # STREET ADDRESS NUMBER
							if types == u'street_number':
								streetNumber.append(place.details['address_components'][9]['long_name'])
								for TheStreetNumber in streetNumber:
									if TheStreetNumber:
										addressStreetNumber = TheStreetNumber.encode('utf-8-sig')
									else: 
										addressStreetNumber = None
		
							  # STREET ADDRESS NAME
							elif types == u'route':
								route0.append(place.details['address_components'][9]['long_name'])
								for route in route0:
									if route:
										addressStreetName = route.encode('utf-8-sig')
									else:
										addressStreetName = None
		
							  # POINT OF INTEREST
							elif types == u'point_of_interest':
								point_of_interest0.append(place.details['address_components'][9]['long_name'])
								for ThePointOfInterest in point_of_interest0:
									if ThePointOfInterest:
										pointOfInterest = ThePointOfInterest.encode('utf-8-sig')
									else:
										pointOfInterest = None
		
							  # PREMISE
							elif types == u'premise':
								premise0.append(place.details['address_components'][9]['long_name'])
								for ThePremise in premise0:
									if ThePremise:
										premise = ThePremise.encode('utf-8-sig')
									else:
										premise = None
		
							  # SUBPREMISE
							elif types == u'subpremise':
								subpremise0.append(place.details['address_components'][9]['long_name'])
								for TheSubpremise in subpremise0:
									if TheSubpremise:
										subpremise = TheSubpremise.encode('utf-8-sig')
									else:
										subpremise = None
		
		
							  # CITY NAME
							elif types == u'locality':
								localityCity0.append(place.details['address_components'][9]['long_name'])
								for locality in localityCity0:
									if locality:
										cityName = locality.encode('utf-8-sig')
									else:
										cityName = None
		
							  # STATE NAME
							elif types == u'administrative_area_level_1':
								adminAreaLevel1State0.append(place.details['address_components'][9]['long_name'])
								for stateName in adminAreaLevel1State0:
									if stateName:
										state = stateName.encode('utf-8-sig')
									else:
										state = None
		
							  # POSTAL CODE
							elif types == u'postal_code':
								postalCode0.append(place.details['address_components'][9]['long_name'])
								for ThePostalCode in postalCode0:
									if ThePostalCode:
										postal_code1 = ThePostalCode.encode('utf-8-sig')
									else:
										postal_code1 = None
		
							  # COUNTRY NAME	
							elif types == u'country':
								countryName0.append(place.details['address_components'][9]['long_name'])
								for countryName in countryName0:
									if countryName:
										countryNameIdentified = countryName.encode('utf-8-sig')
									else:
										countryNameIdentified = None
		
							# Sublocatlity Level 1
							elif types == u'sublocality_level_1':
								sublocalityLevel1.append(place.details['address_components'][9]['long_name'])
								for sublocalityL1 in sublocalityLevel1:
									if sublocalityL1:
										sublocality_area_level_1 = sublocalityL1.encode('utf-8-sig')
									else:
										sublocality_area_level_1 = None
		
							# Sublocatlity Level 2
							elif types =='sublocality_level_2':
								sublocalityLevel2.append(place.details['address_components'][9]['long_name'])
								for sublocalityL2 in sublocalityLevel2:
									if sublocalityL2:
										sublocality_area_level_2 = sublocalityL2.encode('utf-8-sig')
									else:
										sublocality_area_level_2 = None
							
							# Sublocatlity Level 3
							elif types == u'sublocality_level_3':
								sublocalityLevel3.append(place.details['address_components'][9]['long_name'])
								for sublocalityL3 in sublocalityLevel3:
									if sublocalityL3:
										sublocality_area_level_3 = sublocalityL3.encode('utf-8-sig')
									else:
										sublocality_area_level_3 = None
		
							else:
								pass
		
					except Exception, e:
						pass
		
	#######################################################################################################################
	#######################################################################################################################
	#######################################################################################################################
	#######################################################################################################################
	#######################################################################################################################
	#######################################################################################################################
			
					### Finding if there is a Latitude associated with the locaton
					if place.geo_location['lat']:
						Lat = place.geo_location['lat']
					else:
						pass

					### Finding if there is a Longitude associated with the locaton
					if place.geo_location['lng']:
						Lon = place.geo_location['lng']
					else:
						pass

					### There is no location ID as of right now
					location_id = None

					### Name of the location
					if place.name:
						names = place.name
						name = names.encode('utf-8-sig')
					else:
						pass

					### Alternative names can only be found manually
					alt_names = None

					### The type of location this is (POEE, MEDICAL, HOTEL, DIPLOMATIC)
					type_1 = key

					### No Ranking system yet
					type_ranking = None

					### Capabilities can only be found manually
					capabilities = None
	
					### The full address of the place, I havent been able to make this just the number and address yet(which is what it is supposed to be)
					### ... because every country formats their address differently
					if place.details['formatted_address']:
						address1 = place.details['formatted_address']
						address_line1 = address1.encode('utf-8-sig')
					else:
						address_line1 = None
	
					### Incorportes areas of an address like Neighborhood and so forth
					address_line2 = None
	
					### The name of the city that is associated with the location
					try:
						if cityName:
							city = cityName
						else:
							city = None
					except Exception, e:
						city = None
	
					### Postal Code associated with the location
					try:
						if postal_code1:
							postal_code = postal_code1
						else:
							postal_code = None
					except Exception, e:
						postal_code = None
					
					### The state that the location resides in
					try:
						if state:
							adm1 = state
						else:
							adm1 = None
					except:
						adm1 = None
					### The country that the location resides in
					if countryNameIdentified:
						country = countryNameIdentified
					else:
						country = None
					
					### The International phone number of the Location (*If Available)
					if place.international_phone_number:
						phone_number = place.international_phone_number
					else:
						phone_number = None
	
					### The email address of the location must be found manually
					email_address = None
	
					### The website of the location (*If Available)
					if place.website:
						web_address = place.website
					else:
						web_address = None
	
					### Notes must be entered Manually
					notes = None
					
					### This will only be written if 3 conditions are met for a location (Latitude, Longitude, and Name)
					if (Lat and Lon and name):
						row = Lat, Lon, location_id, name, alt_names, type_1, type_ranking, capabilities, address_line1, address_line2, city, postal_code, adm1, country, phone_number, email_address, web_address, notes
						writer.writerow(row)

if __name__ == "__main__":
	main()








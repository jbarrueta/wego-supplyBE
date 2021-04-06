const test = {
  type: "FeatureCollection",
  query: [-97.7526, 30.2289],
  features: [
    {
      id: "address.8384050228111234",
      type: "Feature",
      place_type: ["address"],
      relevance: 1,
      properties: { accuracy: "street" },
      text: "Theatre Pass",
      place_name: "Theatre Pass, Austin, Texas 78704, United States",
      center: [-97.7529333, 30.2289317],
      geometry: { type: "Point", coordinates: [-97.7529333, 30.2289317] },
      context: [
        { id: "neighborhood.2105422", text: "St. Edwards" },
        { id: "postcode.1477377152862310", text: "78704" },
        { id: "place.7902985522754850", wikidata: "Q16559", text: "Austin" },
        {
          id: "district.14251652747735210",
          wikidata: "Q110426",
          text: "Travis County",
        },
        {
          id: "region.12968715825342410",
          wikidata: "Q1439",
          short_code: "US-TX",
          text: "Texas",
        },
        {
          id: "country.19678805456372290",
          wikidata: "Q30",
          short_code: "us",
          text: "United States",
        },
      ],
    },
    {
      id: "neighborhood.2105422",
      type: "Feature",
      place_type: ["neighborhood"],
      relevance: 1,
      properties: {},
      text: "St. Edwards",
      place_name: "St. Edwards, Austin, Texas 78704, United States",
      bbox: [-97.763586, 30.215822, -97.741241, 30.238801],
      center: [-97.75, 30.22],
      geometry: { type: "Point", coordinates: [-97.75, 30.22] },
      context: [
        { id: "postcode.1477377152862310", text: "78704" },
        { id: "place.7902985522754850", wikidata: "Q16559", text: "Austin" },
        {
          id: "district.14251652747735210",
          wikidata: "Q110426",
          text: "Travis County",
        },
        {
          id: "region.12968715825342410",
          wikidata: "Q1439",
          short_code: "US-TX",
          text: "Texas",
        },
        {
          id: "country.19678805456372290",
          wikidata: "Q30",
          short_code: "us",
          text: "United States",
        },
      ],
    },
    {
      id: "postcode.1477377152862310",
      type: "Feature",
      place_type: ["postcode"],
      relevance: 1,
      properties: {},
      text: "78704",
      place_name: "Austin, Texas 78704, United States",
      bbox: [
        -97.8024888312204,
        30.2162014804577,
        -97.7350189902569,
        30.2675280072576,
      ],
      center: [-97.75, 30.26],
      geometry: { type: "Point", coordinates: [-97.75, 30.26] },
      context: [
        { id: "place.7902985522754850", wikidata: "Q16559", text: "Austin" },
        {
          id: "district.14251652747735210",
          wikidata: "Q110426",
          text: "Travis County",
        },
        {
          id: "region.12968715825342410",
          wikidata: "Q1439",
          short_code: "US-TX",
          text: "Texas",
        },
        {
          id: "country.19678805456372290",
          wikidata: "Q30",
          short_code: "us",
          text: "United States",
        },
      ],
    },
    {
      id: "place.7902985522754850",
      type: "Feature",
      place_type: ["place"],
      relevance: 1,
      properties: { wikidata: "Q16559" },
      text: "Austin",
      place_name: "Austin, Texas, United States",
      bbox: [
        -98.0375379944296,
        30.0679421285106,
        -97.5415641434733,
        30.5217759500416,
      ],
      center: [-97.7437, 30.2711],
      geometry: { type: "Point", coordinates: [-97.7437, 30.2711] },
      context: [
        {
          id: "district.14251652747735210",
          wikidata: "Q110426",
          text: "Travis County",
        },
        {
          id: "region.12968715825342410",
          wikidata: "Q1439",
          short_code: "US-TX",
          text: "Texas",
        },
        {
          id: "country.19678805456372290",
          wikidata: "Q30",
          short_code: "us",
          text: "United States",
        },
      ],
    },
    {
      id: "district.14251652747735210",
      type: "Feature",
      place_type: ["district"],
      relevance: 1,
      properties: { wikidata: "Q110426" },
      text: "Travis County",
      place_name: "Travis County, Texas, United States",
      bbox: [-98.172977, 30.024499, -97.369539, 30.628249],
      center: [-97.78, 30.33],
      geometry: { type: "Point", coordinates: [-97.78, 30.33] },
      context: [
        {
          id: "region.12968715825342410",
          wikidata: "Q1439",
          short_code: "US-TX",
          text: "Texas",
        },
        {
          id: "country.19678805456372290",
          wikidata: "Q30",
          short_code: "us",
          text: "United States",
        },
      ],
    },
    {
      id: "region.12968715825342410",
      type: "Feature",
      place_type: ["region"],
      relevance: 1,
      properties: { wikidata: "Q1439", short_code: "US-TX" },
      text: "Texas",
      place_name: "Texas, United States",
      bbox: [
        -106.645478915861,
        25.8372300015839,
        -93.5080380060539,
        36.5004398479541,
      ],
      center: [-98.8223185136653, 31.8039734986],
      geometry: {
        type: "Point",
        coordinates: [-98.8223185136653, 31.8039734986],
      },
      context: [
        {
          id: "country.19678805456372290",
          wikidata: "Q30",
          short_code: "us",
          text: "United States",
        },
      ],
    },
    {
      id: "country.19678805456372290",
      type: "Feature",
      place_type: ["country"],
      relevance: 1,
      properties: { wikidata: "Q30", short_code: "us" },
      text: "United States",
      place_name: "United States",
      bbox: [-179.9, 18.8163608007951, -66.8847646185949, 71.4202919997506],
      center: [-97.9222112121185, 39.3812661305678],
      geometry: {
        type: "Point",
        coordinates: [-97.9222112121185, 39.3812661305678],
      },
    },
  ],
  attribution:
    "NOTICE: © 2021 Mapbox and its suppliers. All rights reserved. Use of this data is subject to the Mapbox Terms of Service (https://www.mapbox.com/about/maps/). This response and the information it contains may not be retained. POI(s) provided by Foursquare.",
};
//Testing getGeocoding "Theatre Pass, Austin, Texas 78704, United States"

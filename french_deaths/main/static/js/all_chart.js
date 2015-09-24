
                        
                          AmCharts.makeChart("chartdiv",
                            {
                              "type": "serial",
                              "categoryField": "date",
                              "dataDateFormat": "YYYY",
                              "theme": "dark",
                              "categoryAxis": {
                                "minPeriod": "YYYY",
                                "parseDates": true
                              },
                              "chartCursor": {
                                "animationDuration": 0,
                                "categoryBalloonDateFormat": "YYYY"
                              },
                              "chartScrollbar": {},
                              "trendLines": [],
                              "graphs": [
                                {
                                  "fillAlphas": 0.7,
                                  "id": "AmGraph-1",
                                  "lineAlpha": 0,
                                  "title": "Men",
                                  "valueField": "Men"
                                },
                                {
                                  "fillAlphas": 0.7,
                                  "id": "AmGraph-2",
                                  "lineAlpha": 0,
                                  "title": "Women",
                                  "valueField": "Women"
                                }
                              ],
                              "guides": [],
                              "valueAxes": [
                                {
                                  "id": "ValueAxis-1",
                                  "title": "Number of deaths"
                                }
                              ],
                              "allLabels": [],
                              "balloon": {},
                              "legend": {},
                              "titles": [
                                {
                                  "id": "Title-1",
                                  "size": 15,
                                  "text": "Deaths in France by gender, 2001-2008"
                                }
                              ],
                              "dataProvider": [
                                {
                                  "date": "2001",
                                  "Men": "277858",
                                  "Women": "263325"
                                },
                                {
                                  "date": "2002",
                                  "Men": "278794",
                                  "Women": "266555"
                                },
                                {
                                  "date": "2003",
                                  "Men": "284729",
                                  "Women": "277858"
                                },
                                {
                                  "date": "2004",
                                  "Men": "268653",
                                  "Women": "250788"
                                },
                                {
                                  "date": "2005",
                                  "Men": "276553",
                                  "Women": "261633"
                                },
                                {
                                  "date": "2006",
                                  "Men": "271406",
                                  "Women": "255160"
                                },
                                {
                                  "date": "2007",
                                  "Men": "273401",
                                  "Women": "257419"
                                },
                                {
                                  "date": "2008",
                                  "Men": "277598",
                                  "Women": "265541"
                                }
                              ]
                            }
                          );
                         


                
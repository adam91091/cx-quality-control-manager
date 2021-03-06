from apps.constants import CLIENT_SAP_DIGITS, PRODUCT_SAP_DIGITS, ORDER_SAP_DIGITS

VIEW_MSG = {'client': {'new_success': "Utworzono nowego klienta",
                       'new_error': "Nie utworzono nowego klienta. "
                                    "Wystąpiły następujące błędy formularza:",
                       'update_success': "Zaktualizowano dane klienta",
                       'update_error': "Nie zaktualizowano danych klienta. "
                                       "Wystąpiły następujące błędy formularza:",
                       'delete_success': "Klient został usunięty", },
            'product': {'new_success': "Utworzono nowy produkt",
                        'new_error': "Nie utworzono nowego produktu. "
                                     "Wystąpiły następujące błędy formularza:",
                        'update_success': "Zaktualizowano dane produktu",
                        'update_error': "Nie zaktualizowano danych produktu",
                        'delete_success': "Produkt został usunięty", },
            'specification': {'issue_error': "Nie wystawiono specyfikacji dla klienta. "
                                             "Wystąpiły nastęþujące błędy formularza:",
                              },
            'order': {'new_success': "Utworzono nowe zlecenie produkcyjne",
                      'new_error': "Nie utworzono nowego zlecenia produkcyjnego. "
                                   "Wystąpiły następujące błędy formularza:",
                      'update_success': "Zaktualizowano dane zlecenia produkcyjnego",
                      'update_error': "Nie zaktualizowano danych zlecenia produkcyjnego. "
                                      "Wystąpiły następujące błędy formularza:",
                      'delete_success': "Zlecenie produkcyjne zostało usunięte", },
            'measurement_report': {'new_success': "Dodano raport pomiarowy",
                                   'new_error': "Raport pomiarowy nie został dodany. "
                                                "Wystąpiły następujące błędy formularza:",
                                   'update_success': "Zaktualizowano raport pomiarowy",
                                   'update_error': "Nie zaktualizowano raportu pomiarowego. "
                                                   "Wystąpiły następujące błędy formularza:",
                                   'close_success': "Pomiary zostały zakończone",
                                   'close_not_saved_error': "Nie można zamknąć raportu pomiarowego, "
                                                            "który nie został zapisany.",
                                   'close_access_error': "Raport pomiarowy już został zamknięty.",
                                   'close_edit_error': "Zamknięte raporty pomiarowe nie podlegają edycji",
                                   },
            'user': {'login_success': 'Logowanie zakończyło się sukcesem',
                     'logout_success': 'Wylogowano z systemu',
                     'login_fail': 'Logowanie zakończone niepowodzeniem. Wystąpiły następujące błędy formularza:',
                     'inactive': "Użytkownik jest nieaktywny i został zablokowany w systemie",
                     'password_change_success': 'Hasło zostało zmienione',
                     'password_change_fail': "Hasło nie zostało zmienione. Wystąpiły następujące błędy formularza:",
                     'email_change_success': "Adres email został zmieniony",
                     'email_change_error': "Adres email nie został zmieniony. Wystąpiły następujące błędy formularza:",
                     }
            }

HINTS = {'client': {'client_sap_id': "Numer SAP musi się składać z {} cyfr "
                                     "oraz nie może być polem pustym".format(CLIENT_SAP_DIGITS),
                    'client_name': "Pole z nazwą klienta nie może być puste", },
         'product': {'product_sap_id': "Numer SAP musi się składać z {} cyfr "
                                       "oraz nie może być polem pustym".format(PRODUCT_SAP_DIGITS),
                     'index': "Indeks produktu powinien być w określonym formacie, np. T1034321/26",
                     'description': "Pole z opisem nie może być puste", },
         'specification': {'remarks': "Pole z uwagami nie może być puste",
                           'float_field': "Podaj liczbę, np. 1 lub 1.0",
                           'integer_field': "Podaj liczbę całkowitą, np. 1",
                           'colour': "Pole z kolorem nie może być puste",
                           'finish': "Pole z powierzchnią zew. nie może być puste",
                           'maximum_height_of_pallet': "Podaj liczbę, np. 1 lub 1.0",
                           'quantity_on_the_pallet': "Podaj całkowitą liczbę sztuk tulei na palecie", },
         'order': {'order_sap_id': "Numer partii musi się składać z {} cyfr "
                                   "oraz nie może być polem pustym".format(ORDER_SAP_DIGITS),
                   'client_sap_id': "Numer SAP musi się składać z {} cyfr "
                                    "oraz nie może być polem pustym".format(CLIENT_SAP_DIGITS),
                   'product_sap_id': "Numer SAP musi się składać z {} cyfr "
                                     "oraz nie może być polem pustym".format(PRODUCT_SAP_DIGITS),
                   'date_of_production': 'Pole z datą produkcji nie może być puste',
                   'quantity': 'Podaj całkowitą liczbę tulei w sztukach',
                   },
         'user': {'username': "Login z pięciu pierwszych liter imienia i "
                              "nazwiska (np. Jan Kowalski - jkowa).",
                  'password': "Przynajmniej 8 znakowe hasło z 1 cyfrą lub więcej.",
                  'lost_password': "Jeśli nie pamiętasz hasła, skontaktuj się z "
                                   "administratorem w celu zresetowania hasła.", }

         }
LABELS = {'client': {'client_sap_id': "Numer SAP klienta",
                     'client_name': "Nazwa klienta", },
          'product': {'product_sap_id': "Numer SAP produktu",
                      'index': "Indeks produktu",
                      'description': "Opis produktu", },
          'specification': {'internal_diameter_target': "Średnica wewnętrzna (mm)",
                            'external_diameter_target': "Średnica zewnętrzna (mm)",
                            'wall_thickness_target': "Grubość ścianki (mm)",
                            'length_target': "Długość (mm)",
                            'flat_crush_resistance_target': "Wytrzymałość na ściskanie (100 MM)",
                            'moisture_content_target': "Wilgotność (%)",
                            'colour': "Kolor",
                            'finish': "Powierzchnia zewnętrzna",
                            'maximum_height_of_pallet': "Maksymalna wysokość palety",
                            'pallet_wrapped_with_stretch_film': "Paleta zabezpieczona folią stretch?",
                            'pallet_protected_with_paper_edges': "Paleta zabezpieczona kątownikami papierowymi?",
                            'cores_packed_in': "Tuleje pakowane:",
                            'quantity_on_the_pallet': "Ilość sztuk na palecie:",
                            'remarks': "Uwagi", },
          'order': {'order_sap_id': "Nr partii",
                    'date_of_production': "Data produkcji",
                    'product': "Kod produktu",
                    'client': "Nr sap klienta",
                    'internal_diameter_reference': "Średnica wewnętrzna",
                    'external_diameter_reference': "Średnica zewnętrzna",
                    'length': "Długość",
                    'quantity': "Ilość", },
          'measurement_report': {'author': "Kontrolował",
                                 'date_of_control': "Data kontroli", },
          'measurement': {'pallet_number': "Paleta nr",
                          'internal_diameter_tolerance_top': "Góra",
                          'internal_diameter_target': "Środek",
                          'internal_diameter_tolerance_bottom': "Dół",
                          'external_diameter_tolerance_top': "Góra",
                          'external_diameter_target': "Środek",
                          'external_diameter_tolerance_bottom': "Dół",
                          'length_tolerance_top': "Góra",
                          'length_target': "Środek",
                          'length_tolerance_bottom': "Dół",
                          'flat_crush_resistance_target': "Kontrola wytrzymałości",
                          'moisture_content_target': "Wilgotność",
                          'weight': "Waga",
                          'remarks': 'Uwagi, klejenie, pakowanie',
                          },
          'user': {'password': "Hasło",
                   'old_password': "Stare hasło",
                   'new_password': "Nowe hasło",
                   'new_password_confirm': "Nowe hasło (powtórz)"}
          }

ERROR_MSG = {'client': {'client_sap_id': {'unique': "Klient o podanym numerze SAP już istnieje.", }, },
             'product': {'product_sap_id': {'unique': "Produkt o podanym numerze SAP już istnieje.", }, },
             'order': {'order_sap_id': {'unique': "Podany nr partii już istnieje.", },
                       'product': {'invalid_choice': 'Produkt o podanym nr SAP nie istnieje w bazie danych.', },
                       'client': {'invalid_choice': 'Klient o podanym nr SAP nie istnieje w bazie danych.', }, },
             'user': {'username': {'unique': "Uzytkownik o podanym loginie już istnieje!.",
                                   'invalid_login': "Podaj właściwy login i hasło. Zwróć uwagę na wielkość znaków.",
                                   'inactive': "Użytkownik o podanym loginie jest nieaktywny.",
                                   },
                      'password': {'required': "To pole jest wymagane"}, },
             }

MODEL_MSG = {'boolean_choices': ["Tak", "Nie", ],
             'cores_packed_in': ["w pozycji pionowej", "w pozycji poziomej", "na kartonach", ],
             'order_status_choices': ["Otwarty", "W trakcie", "Zakończony", ],
             'password': "Wymagane. Musi się skladac z dokladnie 5 liter.",
             }

FORMSET_MSG = {'pallet_number': "Numery palet nie mogą się powtarzać w raporcie pomiarowym!"}

#!/usr/bin/env python

import unicodecsv
import sys

FIELDNAMES = 'reference_number,procurement_id,vendor_name,contract_date,economic_object_code,description_en,description_fr,contract_period_start,delivery_date,contract_value,original_value,amendment_value,comments_en,comments_fr,additional_comments_en,additional_comments_fr,agreement_type_code,commodity_type_code,commodity_code,country_of_origin,solicitation_procedure_code,limited_tendering_reason_code,derogation_code,aboriginal_business,intellectual_property_code,potential_commercial_exploitation,former_public_servant,standing_offer,standing_offer_number,document_type_code,reporting_period,owner_org,owner_org_title'.split(',')

in_csv = unicodecsv.DictReader(sys.stdin, encoding='utf-8')
out_csv = unicodecsv.DictWriter(sys.stdout, fieldnames=FIELDNAMES, encoding='utf-8')
out_csv.writeheader()

for line in in_csv:
    line['procurement_id'] = line.pop('ref_number')
    line['reference_number'] = line.pop('unique_identifier')
    out_csv.writerow(line)

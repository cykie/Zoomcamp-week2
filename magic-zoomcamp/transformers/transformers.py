if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    
    # Specify your transformation logic here
    df_output=data[(data['passenger_count']>0)&(data['trip_distance']>0)]
    df_output['lpep_pickup_date']=df_output['lpep_pickup_datetime'].dt.date
    df_output.rename(columns={"VendorID": "vendor_id"},inplace=True)
    return df_output


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['passenger_count'].isin([0]).sum()==0 , 'There are zero passengers'
    assert output['trip_distance'].isin([0]).sum()==0 , 'There are zero trip distances'
    assert 'vendor_id' in output.columns.any() , 'There is no vendor_id'
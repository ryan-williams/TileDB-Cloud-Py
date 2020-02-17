from . import array

last_udf_task_id = None


class CloudArray(object):
    def apply_async(
        self,
        func,
        ranges,
        attrs=None,
        layout=None,
        image_name=None,
        http_compressor="deflate",
    ):
        """
        Apply a user defined function to an array asynchronous

        **Example**
        >>> import tiledb, tiledb.cloud, numpy
        >>> def median(df):
        ...   return numpy.median(df["a"])
        >>> # Open the array then run the UDF
        >>> with tiledb.SparseArray("tiledb://TileDB-Inc/quickstart_dense", ctx=tiledb.cloud.ctx()) as A:
        ...   A.apply(median, [(0,5), (0,5)], attrs=["a", "b", "c"])
        2.0

        :param func: user function to run
        :param ranges: ranges to issue query on
        :param attrs: list of attributes or dimensions to fetch in query
        :param layout: tiledb query layout
        :param image_name: udf image name to use, useful for testing beta features
        :param http_compressor: set http compressor for results
        :return: UDFResult object which is a future containing the results of the UDF
        """
        return array.apply_async(
            uri=self.uri,
            func=func,
            ranges=ranges,
            attrs=attrs,
            layout=layout,
            image_name=image_name,
            http_compressor=http_compressor,
        )

    def apply(
        self,
        func,
        ranges,
        attrs=None,
        layout=None,
        image_name=None,
        http_compressor="deflate",
    ):
        """
        Apply a user defined function to an array
        :param func: user function to run
        :param ranges: ranges to issue query on
        :param attrs: list of attributes or dimensions to fetch in query
        :param layout: tiledb query layout
        :param image_name: udf image name to use, useful for testing beta features
        :param http_compressor: set http compressor for results
        :return: results of the UDF
        """
        return self.apply_async(
            func=func,
            ranges=ranges,
            attrs=attrs,
            layout=layout,
            image_name=image_name,
            http_compressor=http_compressor,
        ).get()

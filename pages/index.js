import React from 'react'
import Box from 'ui-box'
import Link from 'next/link'
import Head from 'next/head'

export default () => (
  <>
    <Head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous" />
    </Head>
    <Box className='container text-center' height='100vh' width='100vw' display='flex' flexDirection='column' justifyContent='center' alignItems='center'>
      <h1 className='display-3 mb-5'>System Sandobx</h1>
      <Link href='/learn'>
        <a className='btn btn-light mb-2' style={{ width: '50%' }}>
          Learn
        </a>
      </Link>
      <Link href='/play.html'>
        <a className='btn btn-light mb-2' style={{ width: '50%' }}>
          Play
        </a>
      </Link>

      <style jsx>{`
        @import url('https://rsms.me/inter/inter.css');
        :global(html) { font-family: 'Inter', sans-serif; }

        :global(body) {
          margin: 0;
        }
      `}</style>
    </Box>
  </>
)
import React from 'react'
import Head from 'next/head'
import Link from 'next/link'

export default () => (
  <>
    <Head>
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous" />
    </Head>
    <div className='container' width='100vw'>
      <Link href='/'>
        <a className='button'>Back</a>
      </Link>
      <div className='d-flex flex-column justify-content-center align-items-center text-center' style={{ height: '100vh' }}>

      <h1 className='display-3 mb-2'>Learn</h1>
      <p className='lead'>Learn more aobut planets, thingy and thingies.</p>
      </div>
    </div>
  </>
)
test = {
  'name': 'q2_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(simulate_several_key_strikes(15)) == 15
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure your function returns a string.;
          >>> isinstance(simulate_several_key_strikes(15), str)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like your simulation doesn't use all the letters,;
          >>> # or it uses more than the 26 lower-case letters.;
          >>> import numpy as np;
          >>> 26 >= len(np.unique(list(simulate_several_key_strikes(500)))) >= 20
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
